from fastapi.testclient import TestClient
import pytest
import httpx
import json
import asyncio
from httpx import AsyncClient, Response
from app.config import PASSWORD, API_V1_STR
from app.tests.constants import EXPECTED_RESPONSE_BODY, EXPECTED_MULTIPLE_RESPONSE_BODY, BASE_URL
from app.dictionary_service import DictionaryService
from starlette.status import (
    HTTP_403_FORBIDDEN,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_200_OK,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_404_NOT_FOUND,
)
from fastapi.exceptions import ResponseValidationError
from app.main import app

@pytest.fixture
def client():
    """
    Fixture to provide a FastAPI TestClient instance for testing HTTP endpoints.

    Returns:
        TestClient: An instance of TestClient for interacting with FastAPI app.
    """
    return TestClient(app)

@pytest.fixture
def mock_dictionary_service(mocker):
    """
    Fixture to provide a mocked instance of DictionaryService for testing.

    Args:
        mocker: The pytest-mock mocker object.

    Returns:
        MagicMock: A mocked instance of DictionaryService.
    """
    mock = mocker.MagicMock(name="DictionaryService", spec=DictionaryService)
    return mock

def test_get_meaning(client):
    """
    Test case to verify successful retrieval of word meaning.

    Sends a POST request with a word and password to the endpoint and checks if the response status code is 200 OK,
    and the response body matches the expected response body.

    """
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": ["string"], "password": PASSWORD})
    assert response.status_code == HTTP_200_OK
    assert response.json() == EXPECTED_RESPONSE_BODY


def test_missing_word(client):
    """
    Test case to verify handling of missing word in request.

    Sends a POST request without a word but with a password to the endpoint and checks if the response status code
    is 422 Unprocessable Entity.

    """
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"password": PASSWORD})
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_incorrect_password(client):
    """
    Test case to verify handling of incorrect password in request.

    Sends a POST request with a word but an incorrect password to the endpoint and checks if the response status code
    is 403 Forbidden.

    """
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": ["test"], "password": "incorrect"})
    assert response.status_code == HTTP_403_FORBIDDEN



def test_empty_response_from_service(client, mock_dictionary_service):
    """
    Test case to verify handling of empty response from the dictionary service.

    Sends a POST request with a word and password to the endpoint, where the mock dictionary service returns an empty
    meaning for the word. Checks if the response status code is 200 OK and the meaning retrieved is empty.

    """
    word = "test"
    expected_meaning = []

    mock_dictionary_service.get_dictionary_meaning.return_value = expected_meaning

    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": [word], "password": PASSWORD})

    meaning = mock_dictionary_service.get_dictionary_meaning(word)
    mock_dictionary_service.get_dictionary_meaning.assert_called_once_with(word)

    assert response.status_code == HTTP_200_OK
    assert meaning == []


def test_get_meaning_mock(mock_dictionary_service):
    """
    Test case to verify retrieval of word meaning from the mock dictionary service.

    Sets up the mock dictionary service to return a specific meaning for a word, then checks if the meaning retrieved
    matches the expected meaning.

    """
    word = "test"
    expected_meaning = {"partOfSpeech": "noun", "definitions": ["a procedure..."]}
    mock_dictionary_service.get_dictionary_meaning.return_value = expected_meaning

    meaning = mock_dictionary_service.get_dictionary_meaning(word)
    mock_dictionary_service.get_dictionary_meaning.assert_called_once_with(word)

    assert meaning == expected_meaning

def test_get_multiple_word_meaning(client):
    """
    Test case to verify retrieval of meanings for multiple words.

    Sends a POST request with multiple words and password to the endpoint and checks if the response status code is
    200 OK, the number of meanings retrieved matches the expected number, and the meanings match the expected data.

    """
    response = client.post(
        f"{API_V1_STR}/get-word-meaning",
        json={"words": ["hello", "string"], "password": PASSWORD})

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json() == EXPECTED_MULTIPLE_RESPONSE_BODY


@pytest.mark.asyncio
async def test_get_multiple_word_meaning_async(mocker):
    """
    Test case to verify asynchronous retrieval of meanings for multiple words.

    Sets up an asynchronous mock to return a specific response body for the POST request. Then sends an asynchronous
    POST request with multiple words and password to the endpoint and checks if the response status code is 200 OK,
    and if the response body matches the expected response body.

    """
    expected_response_body = EXPECTED_MULTIPLE_RESPONSE_BODY

    async_mock = mocker.AsyncMock(return_value=Response(status_code=200, json=expected_response_body))
    mocker.patch.object(AsyncClient, "post", async_mock)

    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.post(
            f"{API_V1_STR}/get-word-meaning",
            json={"words": ["hello", "string"], "password": PASSWORD}
        )

    assert response.status_code == HTTP_200_OK
    assert response.json() == expected_response_body


def test_get_word_meaning_non_existent_word(client):
    """
    Test case to verify handling of non-existent word in the request.

    Sends a POST request with a non-existent word and password to the endpoint and checks if the response raises
    a ResponseValidationError with status code 422 Unprocessable Entity.

    """
    with pytest.raises(ResponseValidationError):
        response = client.post(
            f"{API_V1_STR}/get-word-meaning",
            json={"words": ["hello", "nongg_gexistent",], "password": PASSWORD}
        )

        assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_encodings(client):
    """
    Test case to verify handling of special characters in word.

    Sends a POST request with a word containing special characters and password to the endpoint and checks if the
    response raises a ResponseValidationError with status code 422 Unprocessable Entity.

    """
    word = "prüfung"
    with pytest.raises(ResponseValidationError):
        response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": [word], "password": PASSWORD})
        assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY

def test_sql_injection(client):
    """
    Test case to verify prevention of SQL injection attack.

    Sends a POST request with a word containing SQL injection code and password to the endpoint. The endpoint should
    prevent SQL injection attacks and raise a ResponseValidationError with status code 422 Unprocessable Entity.

    """
    words = ["hello'; DROP TABLE words;--"]
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": [words], "password": PASSWORD})
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_wrong_method(client):
    """
    Test case to verify handling of incorrect HTTP method.

    Sends a GET request to the endpoint which only accepts POST requests.
    The endpoint should respond with status code 405 Method Not Allowed.

    """
    response = client.get(f"{API_V1_STR}/get-word-meaning")
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_response_format(client):
    """
    Test case to verify the format of the response.

    Sends a POST request with valid data to the endpoint.
    The endpoint should respond with status code 200 OK and the response body should contain 'meanings' key.

    """
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": ["test"], "password": PASSWORD})
    json_data = response.json()
    assert json_data and 'meanings' in json_data[0]


def test_invalid_json(client):
    """
    Test case to verify handling of invalid JSON data in the request body.

    Sends a POST request with invalid JSON data to the endpoint.
    The endpoint should respond with status code 422 Unprocessable Entity.

    """
    response = client.post(f"{API_V1_STR}/get-word-meaning", json="invalid json")
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_case_sensitivity_in_request_body(client):
    """
    Test case to verify handling of case sensitivity in the request body.

    Sends a POST request with words in different cases to the endpoint.
    The endpoint should respond with status code 200 OK and return the correct number of meanings.

    """
    words = ["Test", "test", "TeSt"]
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": words, "password": PASSWORD})

    assert response.status_code == HTTP_200_OK

    try:
        json_data = response.json()
        assert isinstance(json_data, list)
        assert len(json_data) == len(words)
    except json.JSONDecodeError:
        pytest.fail("Response content is not a valid JSON")


def test_special_characters_in_password(client):
    """
    Test case to verify handling of special characters in password.

    Sends a POST request with a password containing special characters to the endpoint.
    The endpoint should correctly handle the special characters and respond with status code 403 Forbidden.

    """
    special_password = "p@ssw0rd!"
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": ["test"], "password": special_password})
    assert response.status_code == HTTP_403_FORBIDDEN


def test_words_with_numbers(client):
    """
    Test case to verify handling of words with numbers.

    Sends a POST request with words containing numbers and a valid password to the endpoint.
    The endpoint should raise a validation error (status code 422 Unprocessable Entity)
    because words with numbers are not allowed according to the API's validation rules.

    """
    words = ["word123", "test456"]
    with pytest.raises(ResponseValidationError):
        response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": words, "password": PASSWORD})
        assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_invalid_route(client):
    """
    Test case to verify handling of requests to an invalid route.

    Sends a POST request to an invalid route with valid data and password to the endpoint.
    The endpoint should respond with status code 404 Not Found.

    """
    response = client.post("/invalid-route", json={"words": ["test"], "password": PASSWORD})
    assert response.status_code == HTTP_404_NOT_FOUND


def test_load(client):
    """
    Test case to verify the load handling capacity of the endpoint.

    Sends multiple concurrent POST requests with the same word and password to the endpoint to simulate a heavy load.
    Checks if all responses have status code 200 OK and if the response body matches the expected response body.

    """
    num_concurrent_requests = 100

    responses = []
    for i in range(num_concurrent_requests):
        response = client.post(
            f"{API_V1_STR}/get-word-meaning",
            json={"words": ["string"], "password": PASSWORD}
        )
        responses.append(response)

    for response in responses:
        assert response.status_code == HTTP_200_OK
        assert response.json() == EXPECTED_RESPONSE_BODY


def test_large_request_body(client):
    """
    Test case to verify handling of a large request body.

    Sends a POST request with a large number of words in the request body to the endpoint.
    The endpoint should respond with status code 422 Unprocessable Entity.

    """
    large_words = ["word"] * 1000
    response = client.post(f"{API_V1_STR}/get-word-meaning", json={"words": large_words, "password": PASSWORD})
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_endpoint_handles_load():
    """
    Test case to verify that the endpoint can handle a high load of requests concurrently.

    Sends multiple concurrent POST requests to the endpoint and checks that each response
    has a status code of 200 OK and contains the expected response body.

    """
    num_requests = 100
    tasks = []
    timeout = httpx.Timeout(30.0, read=60.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        for i in range(num_requests):
            tasks.append(
                asyncio.create_task(
                    client.post(
                        f"{BASE_URL}{API_V1_STR}/get-word-meaning",
                        json={"words": ["string"], "password": PASSWORD}
                    )
                )
            )

        responses = []
        for task in asyncio.as_completed(tasks):
            response = await task
            responses.append(response)

        for response in responses:
            assert response.status_code == HTTP_200_OK

            json_data = response.json()
            assert json_data == EXPECTED_RESPONSE_BODY
