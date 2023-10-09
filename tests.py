import unittest


class EncoderTests(unittest.TestCase):
    def test_caesar_encrypt_typeerror(self):
        self.assertRaises(TypeError, caesar_encrypt, "Hello world!", "offset!")

    def test_caesar_encrypt_valueerror(self):
        self.assertRaises(ValueError, caesar_encrypt, "Hello world!", -25)

    def test_caesar_encrypt_en(self):
        self.assertEqual(caesar_encrypt("Hello, world!", 2), "Jgnnq, yqtnf!")

    def test_caesar_encrypt_ru(self):
        self.assertEqual(caesar_encrypt("Привет, мир!", 2), "Сткджф, окт!")


if __name__ == '__main__':
    unittest.main()
