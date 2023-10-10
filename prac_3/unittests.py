import unittest
from features.steps.encoder import Encoder


class CaesarEncoderTests(unittest.TestCase):
    encoder = Encoder()

    def test_caesar_encrypt_typeerror(self):
        self.assertRaises(TypeError, self.encoder.caesar_encrypt, "Hello world!", "offset!")

    def test_caesar_encrypt_valueerror(self):
        self.assertRaises(ValueError, self.encoder.caesar_encrypt, "Hello world!", -25)

    def test_caesar_encrypt_en(self):
        self.assertEqual(self.encoder.caesar_encrypt("Hello, world!", 2), "Jgnnq, yqtnf!")

    def test_caesar_encrypt_ru(self):
        self.assertEqual(self.encoder.caesar_encrypt("Привет, мир!", 2), "Сткджф, окт!")


class VernamEncoderTests(unittest.TestCase):
    encoder = Encoder()

    def test_vernam_encrypt_typeerror(self):
        self.assertRaises(ValueError, self.encoder.vernam_encrypt, "london!", "system")

    def test_vernam_encrypt_en(self):
        self.assertEqual(self.encoder.vernam_encrypt("london", "system"), "31 22 29 16 10 3")

    def test_vernam_encrypt(self):
        self.assertEqual(self.encoder.vernam_encrypt("hello привет", "!!!!! !!!!!!"), "73 68 77 77 78 0 1054 1121 1049 1043 1044 1123")

class PlayfairEncoderTests(unittest.TestCase):
    encoder = Encoder()

    def test_playfair_encrypt_typeerror(self):
        self.assertEqual(self.encoder.playfair_encrypt("oO,0heh7Mark!", "dyadya"), "NYNIBKRGUG")

    def test_playfair_encrypt(self):
        self.assertEqual(self.encoder.playfair_encrypt("Oh hy Mark", "death"), "NBBXRFUF")

    def test_playfair_encrypt_valueerror(self):
        self.assertRaises(TypeError, self.encoder.playfair_encrypt, "Oh hi Mark", "81327")


if __name__ == '__main__':
    unittest.main()
