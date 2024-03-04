BASE_URL = "http://localhost:8008"

EXPECTED_RESPONSE_BODY = [
        {
            "meanings": [
                {
                    "part_of_speech": "noun",
                    "definitions": [
                        "A building, wing or dependency set apart and adapted for lodging and feeding (and training) animals with hoofs, especially horses.",
                        "(metonymy) All the racehorses of a particular stable, i.e. belonging to a given owner.",
                        "A set of advocates; a barristers' chambers.",
                        "An organization of sumo wrestlers who live and train together.",
                        "A group of prostitutes managed by one pimp."
                    ]
                },
                {
                    "part_of_speech": "noun",
                    "definitions": [
                        "A long, thin and flexible structure made from threads twisted together.",
                        "Such a structure considered as a substance.",
                        "Any similar long, thin and flexible object.",
                        "A thread or cord on which a number of objects or parts are strung or arranged in close and orderly succession; hence, a line or series of things arranged on a thread, or as if so arranged.",
                        "A cohesive substance taking the form of a string.",
                        "A series of items or events.",
                        "The members of a sports team or squad regarded as most likely to achieve success. (Perhaps metaphorical as the \"strings\" that hold the squad together.) Often first string, second string etc.",
                        "In various games and competitions, a certain number of turns at play, of rounds, etc.",
                        "A drove of horses, or a group of racehorses kept by one owner or at one stable.",
                        "An ordered sequence of text characters stored consecutively in memory and capable of being processed as a single entity.",
                        "A stringed instrument.",
                        "(usually in the plural) The stringed instruments as a section of an orchestra, especially those played by a bow, or the persons playing those instruments.",
                        "(in the plural) The conditions and limitations in a contract collectively.",
                        "The main object of study in string theory, a branch of theoretical physics.",
                        "Cannabis or marijuana.",
                        "Part of the game of billiards, where the order of the play is determined by testing who can get a ball closest to the bottom rail by shooting it onto the end rail.",
                        "The buttons strung on a wire by which the score is kept.",
                        "(by extension) The points made in a game of billiards.",
                        "The line from behind and over which the cue ball must be played after being out of play, as by being pocketed or knocked off the table; also called the string line.",
                        "A strip, as of leather, by which the covers of a book are held together.",
                        "A fibre, as of a plant; a little fibrous root.",
                        "A nerve or tendon of an animal body.",
                        "An inside range of ceiling planks, corresponding to the sheer strake on the outside and bolted to it.",
                        "The tough fibrous substance that unites the valves of the pericarp of leguminous plants.",
                        "A small, filamentous ramification of a metallic vein.",
                        "A stringcourse.",
                        "A hoax; a fake story."
                    ]
                },
                {
                    "part_of_speech": "verb",
                    "definitions": [
                        "To put (items) on a string.",
                        "To put strings on (something).",
                        "To form into a string or strings, as a substance which is stretched, or people who are moving along, etc.",
                        "To drive the ball against the end of the table and back, in order to determine which player is to open the game.",
                        "To deliberately state that a certain bird is present when it is not; to knowingly mislead other birders about the occurrence of a bird, especially a rarity; to misidentify a common bird as a rare species."
                    ]
                }
            ],
            "source": [
                "https://en.wiktionary.org/wiki/stable",
                "https://en.wiktionary.org/wiki/string"
            ]
        }
    ]

EXPECTED_MULTIPLE_RESPONSE_BODY = [
  {
    "meanings": [
      {
        "part_of_speech": "noun",
        "definitions": [
          "\"Hello!\" or an equivalent greeting."
        ]
      },
      {
        "part_of_speech": "verb",
        "definitions": [
          "To greet with \"hello\"."
        ]
      },
      {
        "part_of_speech": "interjection",
        "definitions": [
          "A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.",
          "A greeting used when answering the telephone.",
          "A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.",
          "Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.",
          "An expression of puzzlement or discovery."
        ]
      }
    ],
    "source": [
      "https://en.wiktionary.org/wiki/hello"
    ]
  },
  {
    "meanings": [
      {
        "part_of_speech": "noun",
        "definitions": [
          "A building, wing or dependency set apart and adapted for lodging and feeding (and training) animals with hoofs, especially horses.",
          "(metonymy) All the racehorses of a particular stable, i.e. belonging to a given owner.",
          "A set of advocates; a barristers' chambers.",
          "An organization of sumo wrestlers who live and train together.",
          "A group of prostitutes managed by one pimp."
        ]
      },
      {
        "part_of_speech": "noun",
        "definitions": [
          "A long, thin and flexible structure made from threads twisted together.",
          "Such a structure considered as a substance.",
          "Any similar long, thin and flexible object.",
          "A thread or cord on which a number of objects or parts are strung or arranged in close and orderly succession; hence, a line or series of things arranged on a thread, or as if so arranged.",
          "A cohesive substance taking the form of a string.",
          "A series of items or events.",
          "The members of a sports team or squad regarded as most likely to achieve success. (Perhaps metaphorical as the \"strings\" that hold the squad together.) Often first string, second string etc.",
          "In various games and competitions, a certain number of turns at play, of rounds, etc.",
          "A drove of horses, or a group of racehorses kept by one owner or at one stable.",
          "An ordered sequence of text characters stored consecutively in memory and capable of being processed as a single entity.",
          "A stringed instrument.",
          "(usually in the plural) The stringed instruments as a section of an orchestra, especially those played by a bow, or the persons playing those instruments.",
          "(in the plural) The conditions and limitations in a contract collectively.",
          "The main object of study in string theory, a branch of theoretical physics.",
          "Cannabis or marijuana.",
          "Part of the game of billiards, where the order of the play is determined by testing who can get a ball closest to the bottom rail by shooting it onto the end rail.",
          "The buttons strung on a wire by which the score is kept.",
          "(by extension) The points made in a game of billiards.",
          "The line from behind and over which the cue ball must be played after being out of play, as by being pocketed or knocked off the table; also called the string line.",
          "A strip, as of leather, by which the covers of a book are held together.",
          "A fibre, as of a plant; a little fibrous root.",
          "A nerve or tendon of an animal body.",
          "An inside range of ceiling planks, corresponding to the sheer strake on the outside and bolted to it.",
          "The tough fibrous substance that unites the valves of the pericarp of leguminous plants.",
          "A small, filamentous ramification of a metallic vein.",
          "A stringcourse.",
          "A hoax; a fake story."
        ]
      },
      {
        "part_of_speech": "verb",
        "definitions": [
          "To put (items) on a string.",
          "To put strings on (something).",
          "To form into a string or strings, as a substance which is stretched, or people who are moving along, etc.",
          "To drive the ball against the end of the table and back, in order to determine which player is to open the game.",
          "To deliberately state that a certain bird is present when it is not; to knowingly mislead other birders about the occurrence of a bird, especially a rarity; to misidentify a common bird as a rare species."
        ]
      }
    ],
    "source": [
      "https://en.wiktionary.org/wiki/stable",
      "https://en.wiktionary.org/wiki/string"
    ]
  }
]