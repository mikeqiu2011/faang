def find_two_sum(nums, target):
    length = len(nums)

    for i in range(length):
        num_to_find = target - nums[i]
        for j in range(i + 1, length):
            if nums[j] == num_to_find:
                return [i, j]

    return None


nums = [1, 3, 7, 9, 2]
nums = []
target = 11

result = find_two_sum(nums, target)

print(result)
