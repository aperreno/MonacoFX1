"""

A program that converts a Roman numeral to an integer.


"""

ROMAN_NUMERALS = {

    'I': 1,

    'V': 5,

    'X': 10,

    'L': 50,

    'C': 100,

    'D': 500,

    'M': 1000,

}


def jls_extract_def(TEST_CASES):
    for test_input, expected in TEST_CASES:
        result = roman_to_int(test_input)
        if result == expected:
            print('PASS')
        else:
            print('FAIL: {} should be {}'.format(result, expected))
    return result


def roman_to_int(roman):

    """Convert a Roman numeral to an integer."""

    result = 0

    for i in range(len(roman)):

        if i > 0 and ROMAN_NUMERALS[roman[i]] > ROMAN_NUMERALS[roman[i - 1]]:

            result += ROMAN_NUMERALS[roman[i]] - 2 * ROMAN_NUMERALS[roman[i - 1]]

        else:

            result += ROMAN_NUMERALS[roman[i]]

    return result

TEST_CASES = [

    ('I', 1),

    ('III', 3),

    ('IV', 4),

    ('V', 5),

    ('VI', 6),

    ('IX', 9),

    ('X', 10),

    ('XI', 11),

    ('XIV', 14),

    ('XIX', 19),

    ('XX', 20),

    ('XL', 40),

    ('L', 50),

    ('LX', 60),

    ('XC', 90),

    ('C', 100),

    ('CD', 400),

    ('D', 500),

    ('CM', 900),

    ('M', 1000),

    ('MCMXCIX', 1999),

    ('MMXIV', 2014),

]

for test_input, expected in TEST_CASES:

    result = roman_to_int(test_input)

    print(result, result == expected)
    