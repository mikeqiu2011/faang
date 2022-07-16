def find_two_sum(nums, target):
    length = len(nums)
    table = {}

    for i in range(length):
        num_to_find = target - nums[i]
        if nums[i] in table:
            return i, table[nums[i]]

        table[num_to_find] = i

    return None


nums = [1, 3, 7, 9, 2]
# nums = []
target = 11

result = find_two_sum(nums, target)

print(result)
