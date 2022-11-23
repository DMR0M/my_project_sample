import unittest
from format_name import get_user_fullname


class NamesTestCase(unittest.TestCase):
    """Test for 'format_name.py'"""

    def test_first_last_name(self):
        formatted_name = get_user_fullname('Rommel', 'Dela Merced')
        self.assertEqual(formatted_name, 'Rommel Dela Merced')


if __name__ == '__main__':
    unittest.main()

