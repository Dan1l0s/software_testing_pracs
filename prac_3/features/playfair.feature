Feature: use playfair method to decrypt a string
    Scenario: decrypt a string with correct input
        Given a running encoder object (playfair)
        When a NBBXRFUF and keyword death are provided (playfair)
        Then decrypted playfair string should be equal to OHHYMARK
        
    Scenario: decrypt a string with non-satisfying input
        Given a running encoder object (playfair)
        When a IFNVMPYMQMKZ and keyword black are provided (playfair)
        Then decrypted playfair string should be equal to HELXLOWORLDX

    Scenario: decrypt a string with incorrect keyword
        Given a running encoder object (playfair)
        When a OhhiMark and keyword 81327 are provided (playfair)
        Then playfair decrypt function should raise a TypeError