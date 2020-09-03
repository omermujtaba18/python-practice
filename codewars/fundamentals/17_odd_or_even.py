import unittest


def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


class Test(unittest.TestCase):

    def test_odd_or_even(self):
        self.assertEqual(odd_or_even([0, 1, 2]), "odd")
        self.assertEqual(odd_or_even([0, 1, 3]), "even")
        self.assertEqual(odd_or_even([1023, 1, 2]), "even")


if __name__ == '__main__':
    unittest.main()
