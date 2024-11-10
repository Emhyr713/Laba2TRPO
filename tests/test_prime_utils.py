# tests/test_prime_utils.py

import unittest
from prime_utils import is_prime 

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        """Тестирует простые числа."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))

    def test_non_prime_numbers(self):
        """Тестирует составные числа."""
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12)) 
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(18))

    def test_negative_numbers_and_zero(self):
        """Тестирует ноль и отрицательные числа."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-10))

if __name__ == '__main__':
    unittest.main()
