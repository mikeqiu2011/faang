def get_two_indices_with_most_water(nums):
    length = len(nums)

    # left = nums[0]
    # right = nums[length-1]
    max_area = 0

    i = 0
    j = length - 1
    while(i<j):
        width = j - i
        height = min(nums[i],nums[j])
        area = width * height
        max_area = max(area, max_area)
        if nums[i] <= nums[j]:
            i += 1
        else:
            j -= 1

    return max_area

nums = [4,8,1,2,3,9]
# nums = []


result = get_two_indices_with_most_water(nums)
print(result)