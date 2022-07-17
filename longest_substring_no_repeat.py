def get_longest_non_repeat_substring(string):
    longest = 0
    result = ''
    for i in range(len(string)):
        temp = string[i]
        for j in range(i+1, len(string)):
            if string[j] not in temp:
                temp += string[j]
            else:
                break

        print(temp)
        if len(temp) > longest:
            result = temp
            longest = len(temp)

    return longest, result



string = 'abcbbd'

lss = get_longest_non_repeat_substring(string)
print(lss)