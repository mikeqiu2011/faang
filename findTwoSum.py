def findTwoSum(nums, target):
    length = len(nums)
    if length <= 1:
        return None

    for i in range(length):
        for j in range(i, length):
            if nums[i] + nums[j] == target:
                return (i,j)

    return None

nums = [1,3,7,9,2]
target = 11

result = findTwoSum(nums,target)

print(result)