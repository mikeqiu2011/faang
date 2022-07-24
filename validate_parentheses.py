def validate_parentheses(string):
    if not string:
        return True

    stack = []
    left = ['(','{','[']
    right = [')','}',']']
    for s in string:
        if s in left:
            stack.append(s)
        elif s in right:
            if len(stack) == 0:
                return False
            prev = stack.pop()
            if not is_pair(prev, s):
                return False
        else:
            print('invalid input')
            return False

    print(stack)
    if len(stack): # there is still item in the stack:
        return False

    return True


def is_pair(left, right):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    if left not in pairs:
        return False

    return pairs[left] == right

if __name__ == '__main__':
    test = '({[]})'
    test = ''
    test = '({[]})]'
    test = '[({[]})'
    test = '{[(])}'
    test = '{[]()}'

    result = validate_parentheses(test)
    print(result)

    # print(is_pair('p',']'))