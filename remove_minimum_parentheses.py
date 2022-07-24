import re
def minimum_parenthese_to_remove(string: str):
    left = 0
    right = len(string) - 1

    pairs = {
        '(': ')',
    }

    result_left = []
    result_right = []

    while left < right:
        while string[left] != '(':
            left_char = string[left]

            if left_char.isalpha():
                result_left.append(left_char)

            left += 1

        while string[right] != ')' and right > left:
            right_char = string[right]

            if right_char.isalpha():
                result_right.append(right_char)

            right -= 1

        if string[left] == '(' and string[right] == ')':
            result_left.append(string[left])
            result_right.append(string[right])
            left += 1
            right -= 1
        else:
            left += 1

    print(result_left, result_right)

    for i in range(len(result_right)-1, -1, -1):
        result_left.append(result_right[i])

    print(result_left)
    return result_left





test = 'a)bc(d)'
test = '))(('
test = ')(ab)('
test = ')(ab(('
minimum_parenthese_to_remove(test)

