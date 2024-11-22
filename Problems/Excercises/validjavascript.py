### Sloth Problem of the Week - Nov 21, 2024
'''In JavaScript, there are two types of comments:
Single-line comments start with //
Multi-line or inline comments start with /* and end with */
The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can be no single-line comments in between multi-line comments in between the /* and */.
Create a function that returns True if comments are properly formatted, and False otherwise.'''



def is_valid_javascript(text_input):
    """
    Validate if the input string represents a sequence of valid JavaScript comment patterns.
    Sloth Problem of the Week - Nov 21, 2024
    """

    if len(text_input) % 2 != 0 or len(text_input) < 2:
        return False
    is_open_command = False

    for i in range(0, len(text_input) - 1, 2):

        curr_input = text_input[i:i+2]

        if curr_input not in {'//', '/*', '*/'}:
            return False

        if curr_input == '/*':
            if is_open_command:
                return False
            is_open_command = True

        if curr_input == '*/':
            if not is_open_command:
                return False
            is_open_command = False

    return not is_open_command

if __name__=='__main__':
    test_cases = [
        "//////",
        "/**//**////**/",
        "/**//**////**//*",
        "///*/**/",
        "/////",
        "/",
        "",
        "abc*e!!dc/",
        "/*",
        "*/",
        '* /'
    ]

    for test in test_cases:
        print(f"{test!r} -> {is_valid_javascript(test)}")
