def get_string_after_backspace(string, result):
    index = string.rfind('#')

    if(index == -1):
        for i in range(len(string)-1, -1, -1):
            result.append(string[i])
        return

    for i in range(len(string)-1, index, -1):
        result.append(string[i])

    i = index
    count_of_hash = 0
    while(string[i] == '#'):
        count_of_hash += 1
        i -= 1

    print(count_of_hash)
    print(i)

    i -= count_of_hash
    if i < 0:
        return

    get_string_after_backspace(string[:i+1], result)




string = 'zx#ab#c'
result = []

get_string_after_backspace(string, result)
print(result)