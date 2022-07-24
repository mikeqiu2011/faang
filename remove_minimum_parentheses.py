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

def minimum_parenthese_to_remove2(string: str):
    left_stack = []
    right_stack = []
    for i, s in enumerate(string):
        if s == '(':
            left_stack.append(i)
        elif s == ')':
            if len(left_stack):
                left_stack.pop()
            else:
                right_stack.append(i)

    print(left_stack, right_stack)

    li = left_stack + right_stack
    result = []

    for i, s in enumerate(string):
        if i not in li:
            result.append(string[i])

    return result




test = 'a)bc(d)'
test = '))(('
test = ')(ab)('
# test = ')(ab(('
result = minimum_parenthese_to_remove2(test)

print(result)

