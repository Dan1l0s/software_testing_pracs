Feature: use caesar method to decrypt a string
    Scenario: decrypt an eng string
        Given a running encoder object (vijn)
        When a Rijvs, qw ambpb and KEY are provided (vijn)
        Then decrypted (vijn) string should be equal to Hello, my world
    
    Scenario: decrypt a ru string
        Given a running encoder object (vijn)
        When a Икхиюм, еиц евэ and ключ are provided (vijn)
        Then decrypted (vijn) string should be equal to Привет, мой мир
        
    Scenario: decrypt a string with incorrect input
        Given a running encoder object (vijn)
        When a Hello world! and empty are provided (vijn)
        Then decrypt (vijn) function should raise a value error