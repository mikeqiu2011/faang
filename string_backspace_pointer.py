def compare_string(str1, str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1

    while p1 >= 0 or p2 >= 0:
        if str1[p1] == '#' or str2[p2] == '#':
            if str1[p1] == '#':
                cnt_str1_hash = 2
                while(cnt_str1_hash > 0):
                    p1 -= 1
                    cnt_str1_hash -= 1
                    if str1[p1] == '#':
                        cnt_str1_hash += 2

            if str2[p2] == '#':
                cnt_str2_hash = 2
                while (cnt_str2_hash > 0):
                    p2 -= 1
                    cnt_str2_hash -= 1
                    if str2[p2] == '#':
                        cnt_str2_hash += 2

        else:
            if str1[p1] != str2[p2]:
                return False

            p1 -= 1
            p2 -= 1


    return True


string1 = 'zb##c'
string2 = 'c#zx#c'


result = compare_string(string1, string2)
print(result)