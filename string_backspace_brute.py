def get_string_after_backspace(string):
    result = []
    i = 0
    while i < len(string):
        char = string[i]
        if char != '#':
            result.append(char)
        else:
            if len(result) > 0:
                result.pop()
        i += 1

    return result


def compare_string(str1, str2):
    str1 = get_string_after_backspace(str1)
    str2 = get_string_after_backspace(str2)

    print(str1)
    print(str2)

    return str1 == str2


string1 = 'zx#ab#####c'
string2 = 'zag####c'


result = compare_string(string1, string2)
print(result)