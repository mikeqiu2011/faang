def calc_rainwater_to_trap(tanks):
    sum = 0
    i = 0
    j = 1
    limit = len(tanks)
    while j < limit-1:
        if tanks[i] == 0:
            i += 1

        j = i+1
        while (tanks[j] < tanks[i]) and (j < limit-1):
            j += 1

        print(tanks[i:j+1])
        area = calc_area(tanks[i:j+1])
        sum += area

        i = j

    return sum

def calc_area(closure):
    width = len(closure) - 2
    height = min(closure[0], closure[-1])
    obstacle_area = sum(closure[1:-1])
    return width * height - obstacle_area

# closure = [1,0,2]
# closure = [2,1,0,3]
# closure = [3,1,0,1,2]
# result = calc_area(closure)
# print(result)

tanks = [0,1,0,2,1,0,3,1,0,1,2]
tanks = [0,1,0,2,1,0,3,1,0,1,1]
# tanks = [3,4,3]
result = calc_rainwater_to_trap(tanks)
print(result)
