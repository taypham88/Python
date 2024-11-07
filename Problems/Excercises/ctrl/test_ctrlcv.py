import pytest
from ctrl import ctrlCV  # Replace `your_module` with the actual module name if needed

class TestCtrlCV:

    def test_basic_copy_paste(self):
        # Test basic copy and paste functionality
        assert ctrlCV('the egg and Ctrl + C Ctrl + V the spoon') == ['the', 'egg', 'and', 'the', 'egg', 'and', 'the', 'spoon']

    def test_warning_copy_paste(self):
        # Test copy without actual content, then paste
        assert ctrlCV('WARNING Ctrl + V Ctrl + C Ctrl + V') == ['WARNING','WARNING']

    def test_complex_copy_paste(self):
        # Test multiple copy-paste operations
        assert ctrlCV('The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V') == ['The', 'The', 'Town', 'The', 'The', 'Town']

    def test_no_commands(self):
        # Test input with no copy or paste commands
        assert ctrlCV('hello world') == ['hello', 'world']

    def test_copy_without_paste(self):
        # Test copy command without any paste afterward
        assert ctrlCV('hello Ctrl + C world') == ['hello', 'world']

    def test_paste_without_copy(self):
        # Test paste command without any copy before it
        assert ctrlCV('hello Ctrl + V world') == ['hello', 'world']

    def test_empty_string(self):
        # Test an empty input string
        assert ctrlCV('') == ['']

    def test_multiple_copy_and_paste(self):
        # Test with multiple copy-paste sequences
        assert ctrlCV('one two Ctrl + C Ctrl + V three Ctrl + V') == ['one', 'two', 'one', 'two', 'three']

    def test_repeated_copy_overwrites(self):
        # Test repeated copy overwrites previous copy
        assert ctrlCV('alpha beta Ctrl + C gamma Ctrl + C Ctrl + V') == ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma']