import unittest


def title_case(title, minor_words=''):
    if minor_words == '':
        return title.title()
    else:
        output = []
        for index, word in enumerate(title.split()):
            if index == 0 or word.lower() not in (minor.lower() for minor in minor_words.split()):
                output.append(word.title())
            else:
                output.append(word.lower())

        return " ".join(output)


class Test(unittest.TestCase):

    def test_title_case_1(self):
        self.assertEqual(title_case(''), '')

    def test_title_case_2(self):
        self.assertEqual(title_case('a clash of KINGS',
                                    'a an the of'), 'A Clash of Kings')

    def test_title_case_3(self):
        self.assertEqual(title_case('THE WIND IN THE WILLOWS',
                                    'The In'), 'The Wind in the Willows')

    def test_title_case_4(self):
        self.assertEqual(title_case('the quick brown fox'),
                         'The Quick Brown Fox')


if __name__ == '__main__':
    unittest.main()
