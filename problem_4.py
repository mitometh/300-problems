# This problem was asked by Facebook.
# Given a number in Roman numeral format, convert it to decimal.
# The values of Roman numerals are as follows:
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
# For the input XIV, for instance, you should return 14

def solve(roman_number):
    mapping = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total = 0
    previous_value = 0

    # Roman numerals always start with the largest value and go to the smallest.
    # If a smaller numeral stands before a larger numeral, it indicates subtraction.
    # Therefore, we check if the previous numeral is less than the current numeral.
    # If so, the value should be the current value minus the previous value.

    for char in reversed(roman_number):
        current_value = mapping[char]
        if current_value >= previous_value:
            total += current_value
        else:
            total -= current_value
        previous_value = current_value

    return total

if __name__ == '__main__':
    print(solve("IV"))  # Output should be 4
    print(solve("XIV"))  # Output should be 14
    print(solve("LXXX"))  # Output should be 80