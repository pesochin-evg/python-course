import unittest
from solution import sum_pair


class TestSumPair(unittest.TestCase):

    def test_basic_case(self):
        result = sum_pair([2, 7, 11, 15], 9)
        self.assertEqual(result, (0, 1))

    def test_another_case(self):
        result = sum_pair([3, 2, 4], 6)
        self.assertEqual(result, (1, 2))

    def test_same_number(self):
        result = sum_pair([3, 3], 6)
        self.assertEqual(result, (0, 1))

if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=2)