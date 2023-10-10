Feature: use vernam method to decrypt a string
    Scenario: decrypt an string
        Given a running vernam encoder object
        When a 31 22 29 16 10 3 and system are provided to vernam encoder
        Then decrypted string by vernam encoder should be equal to london
        
    Scenario: decrypt a string by vernam encoder with incorrect input
        Given a running vernam encoder object
        When a 31 22 29 qq 16 10 and system are provided to vernam encoder
        Then vernam encoder should raise a value error

    Scenario: decrypt a string by vernam encoder with incorrect key
        Given a running vernam encoder object
        When a 31 22 29 16 16 10 and system1 are provided to vernam encoder
        Then vernam encoder should raise a value error