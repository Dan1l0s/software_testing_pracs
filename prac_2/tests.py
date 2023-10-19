import unittest

import functions


class TestCases(unittest.TestCase):
    def test_check_dot_in_circle(self):
        result = functions.check_dot_in_circle(1.1, 0, 1.1)
        self.assertEqual(result, "On the circle")

        result = functions.check_dot_in_circle(0, 0, 1.1)
        self.assertEqual(result, "Inside")

        result = functions.check_dot_in_circle(1, 1, 1.1)
        self.assertEqual(result, "Outside")

    def test_rgb_to_hex(self):
        self.assertEqual(functions.rgb_to_hex(123, 31, 123), "#7B1F7B")
        self.assertEqual(functions.rgb_to_hex(-25, 0, 260), "Colors must have 0-255 values")
        self.assertEqual(functions.rgb_to_hex(255, 0, 255), "#FF00FF")

    def test_check_dot_in_quadrangle(self):
        result = functions.check_dot_in_quadrangle([3, 3], [0, 0], [5, 0], [5, 5], [0, 5])
        self.assertEqual(result, 1)

        result = functions.check_dot_in_quadrangle([5, 2.5], [5, 5], [5, 0], [0, 5], [0, 0])
        self.assertEqual(result, 0)

        result = functions.check_dot_in_quadrangle([7, 7], [5, 5], [5, 0], [0, 0], [0, 5])
        self.assertEqual(result, -1)

    def test_check_prime(self):
        self.assertEqual(functions.check_prime(1), False)
        self.assertEqual(functions.check_prime(2372632), False)
        self.assertEqual(functions.check_prime(997), True)

    def test_get_gcd(self):
        self.assertEqual(functions.get_gcd(25, 8), 1)
        self.assertEqual(functions.get_gcd(256, 384), 128)
        self.assertEqual(functions.get_gcd(1000, 7), 1)

    def test_get_joint_length(self):
        self.assertEqual(functions.get_joint_length(0, 0, 1, 5), "No common ground")
        self.assertEqual(functions.get_joint_length(1, 6, -5.5, 2), 1)
        self.assertEqual(functions.get_joint_length(6, 1, -5.5, 20), 5)

    def test_fast_power(self):
        self.assertEqual(functions.fast_power(0.5, 10), 0.0009765625)
        self.assertEqual(functions.fast_power(1.5, 4), 5.0625)
        self.assertEqual(functions.fast_power(2.5, 4), 39.0625)

    def test_generate_primes(self):
        self.assertEqual(functions.generate_primes(1), [])
        self.assertEqual(functions.generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(functions.generate_primes(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])


if __name__ == '__main__':
    unittest.main()
