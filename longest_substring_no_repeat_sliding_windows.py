def get_longest_non_repeat_substring(string):
    longest = 0

    final_left = 0
    final_right = 0

    left = 0
    right = 0

    hashmap = {}

    length = len(string)

    while right < length:
        char = string[right]
        if char not in hashmap:
            hashmap[char] = right
            right += 1
        else:
            cur_length = right - left
            if cur_length > longest:
                longest = cur_length
                final_left = left
                final_right = right

            gap = hashmap[char] - left + 1
            left += gap
            right += gap
            continue

    cur_length = right - left
    if cur_length > longest:
        longest = cur_length
        final_left = left
        final_right = right

    return longest, string[final_left:final_right]



string = 'abcbbd'
string = 'abcdbghi'
string = 'abcdcahi'

lss = get_longest_non_repeat_substring(string)
print(lss)