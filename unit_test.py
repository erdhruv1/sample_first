import unittest
from sum123 import sum

class SimpleTest(unittest.TestCase):

    def test_sum_method(self):
        self.assertEqual(sum(2, 3), 5)

if __name__ == '__main__':
    unittest.main()