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
            if not isPair(prev, s):
                return False
        else:
            print('invalid string')

    print(stack)
    if len(stack): # there is still item in the stack:
        return False

    return True


def isPair(left, right):
    if left == '[' and right == ']':
        return True
    elif left == '(' and right == ')':
        return True
    elif left == '{' and right == '}':
        return True
    else:
        return False

if __name__ == '__main__':
    test = '({[]})'
    test = ''
    test = '({[]})]'
    test = '[({[]})'

    result = validate_parentheses(test)
    print(result)