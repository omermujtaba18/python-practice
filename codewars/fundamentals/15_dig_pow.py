import unittest


def dig_pow(n, p):

    sum = 0
    for i, c in enumerate(str(n)):
        sum += pow(int(c), p+i)

    return sum/n if sum % n == 0 else -1


class TestDigPow(unittest.TestCase):

    def test_dig_pow(self):
        self.assertEqual(dig_pow(92, -1), -1)


if __name__ == "__main__":
    unittest.main()
