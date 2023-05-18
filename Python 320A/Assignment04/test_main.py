'''Test for misc main.py functions'''

#pylint: disable=W0613, R0201
import unittest
from unittest.mock import patch
import main

class TestMiscMain(unittest.TestCase):
    '''
    misc main.py Testing
    '''

    @patch('builtins.input', side_effect = \
        ['y', 'purple', 'Yes', 'YES','yEs', 'red', 'n', 'NO', '12', 'nO', 'N'])
    def test_yes_or_no(self, mock_print):
        '''Test for yes or no input handling function'''

        test = main.yes_or_no("test")
        assert test is True

        test = main.yes_or_no("test")
        assert test is True

        test = main.yes_or_no("test")
        assert test is True

        test = main.yes_or_no("test")
        assert test is True

        test = main.yes_or_no("test")
        assert test is False

        test = main.yes_or_no("test")
        assert test is False

        test = main.yes_or_no("test")
        assert test is False

        test = main.yes_or_no("test")
        assert test is False
