Feature: use caesar method to decrypt a string
    Scenario: decrypt an eng string
        Given a running encoder object
        When a Jgnnq yqtnf! and 2 are provided
        Then decrypted string should be equal to Hello world!
    
    Scenario: decrypt a ru string
        Given a running encoder object
        When a Гдьхшё, аьд! and 20 are provided
        Then decrypted string should be equal to Привет, мир!
        
    Scenario: decrypt a string with incorrect input
        Given a running encoder object
        When a Hello world! and -5 are provided
        Then decrypt function should raise a value error