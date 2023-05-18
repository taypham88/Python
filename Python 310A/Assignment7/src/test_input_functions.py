# Test file for input_functions

import input_functions as ip
import unittest
from unittest.mock import patch

class TestInputs(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['y', 'purple', 'Yes', 'YES','yEs', 'red', 'n', 'NO', '12', 'nO', 'N'])
    def test_yes_or_no(self, mock_input, mock_print):
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == True)
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == True)

        test = ip.yes_or_no("test")
        self.assertTrue(test == True)
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == True)

        test = ip.yes_or_no("test")
        self.assertTrue(test == False)
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == False)
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == False)
        
        test = ip.yes_or_no("test")
        self.assertTrue(test == False)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['2021-08-01', '3242', '01-01-2000','1988-01-01'])
    def test_date_entry(self, mock_input, mock_print):     
        
        test = ip.date_entry("test")
        self.assertTrue(test == '2021-08-01')
        
        test = ip.date_entry("test")
        self.assertTrue(test == '1988-01-01')
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['','123456789101213141516171819101213','text','Pass Test'])
    def test_text_input(self, mock_input, mock_print):     
        
        test = ip.text_input("test")
        self.assertTrue(test == 'text')
        
        test = ip.text_input("test")
        self.assertTrue(test == 'Pass Test')

    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['','-1','10000','black','5','100'])
    def test_check_integer(self, mock_input, mock_print):
        
        test = ip.check_integer("test")
        self.assertTrue(test == 5)

        test = ip.check_integer("test")
        self.assertTrue(test == 100)       

if __name__=='__main__':
    unittest.main()       
        