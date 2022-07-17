def get_longest_non_repeat_substring(string):
    seen = {}
    left = 0
    right = 0
    longest = 0

    while right < len(string):
        char = string[right]
        if (char in seen) and (seen[char] >= left):
            left = seen[char] + 1

        seen[char] = right
        longest = max(longest, right - left + 1)
        right += 1

    return longest


string = 'abcbbd'
# string = 'abcdbghi'
string = 'abcdcahi'
string = 'abcbdaac'

lss = get_longest_non_repeat_substring(string)
print(lss)