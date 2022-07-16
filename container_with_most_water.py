def get_two_indices_with_most_water(nums):
    length = len(nums)

    max_area = 0
    left = 0
    right = 0

    for i in range(length):
        for j in range(i+1, length):
            width = j - i
            height = min(nums[i], nums[j])
            area = width*height
            if area > max_area:
                max_area = area
                left = nums[i]
                right = nums[j]

    return left, right, max_area

nums = [1,7,2,8,1,6]
nums = []


result = get_two_indices_with_most_water(nums)
print(result)