import unittest
import primes as p

class PrimesTestCase(unittest.TestCase):

    def test_there_are_25_primes_under_100(self):
        count= p.prime_count(0,100)
        self.assertEqual(25,count)

    def test_0_is_not_prime(self):
        self.assertFalse(p.is_prime(0))


unittest.main()