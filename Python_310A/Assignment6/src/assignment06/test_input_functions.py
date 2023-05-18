import unittest
import input_functions as ip
import mock

class InputTestCase(unittest.TestCase):
    with mock.patch('builtins.input', return_value = 100):
        assert ip.check_integer("this is a question") == 100
        
    with mock.patch('builtins.input', return_value = 9999):
        assert ip.check_integer("this is a question") == 9999

    with mock.patch('builtins.input', return_value = 0):
        assert ip.check_integer("this is a question") == 0

    with mock.patch('builtins.input', return_value = 'y'):
        assert ip.yes_or_no("this is a question") == True
        
    with mock.patch('builtins.input', return_value = 'yes'):
        assert ip.yes_or_no("this is a question") == True

    with mock.patch('builtins.input', return_value = 'Y'):
        assert ip.yes_or_no("this is a question") == True
        
    with mock.patch('builtins.input', return_value = 'Yes'):
        assert ip.yes_or_no("this is a question") == True

    with mock.patch('builtins.input', return_value = 'n'):
        assert ip.yes_or_no("this is a question") == False

    with mock.patch('builtins.input', return_value = 'no'):
        assert ip.yes_or_no("this is a question") == False

    with mock.patch('builtins.input', return_value = 'No'):
        assert ip.yes_or_no("this is a question") == False

    with mock.patch('builtins.input', return_value = 'N'):
        assert ip.yes_or_no("this is a question") == False

    with mock.patch('builtins.input', return_value = '2012-01-01'):
        assert ip.date_entry("this is a question") == '2012-01-01'
        


if __name__ == '__main__':
    unittest.main()