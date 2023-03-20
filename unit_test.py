import unittest


class Testing(unittest.TestCase):

    def test_sum(self):
        sum = 4+5
        self.assertEqual(sum, 9)
