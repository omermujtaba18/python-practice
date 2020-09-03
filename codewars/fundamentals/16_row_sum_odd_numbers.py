import unittest


def row_sum_odd_numbers(n):
    return n**3


class TestRowSumOddNumbers(unittest.TestCase):

    def test_row_sum_odd_numbers(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)


# if __name__ == '__main__':
#     unittest.main()
