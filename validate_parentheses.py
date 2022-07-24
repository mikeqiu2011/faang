def validate_parentheses(string):
    if not string:
        return True

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []

    for s in string:
        if s in pairs:
            stack.append(s)
        elif s in pairs.values():
            if len(stack) == 0:
                return False
            left_bracket = stack.pop()
            correct_bracket = pairs[left_bracket]
            if s != correct_bracket:
                return False
        else:
            print('invalid input')
            return False

    print(stack)
    return len(stack) == 0


if __name__ == '__main__':
    test = '({[]})'
    test = ''
    test = '({[]})]'
    test = '[({[]})'
    test = '{[(])}'
    test = '{[())}'
    # test = '{[]()}'

    result = validate_parentheses(test)
    print(result)

    # print(is_pair('p',']'))