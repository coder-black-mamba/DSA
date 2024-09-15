

def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    for index, item in enumerate(nums):
        left_sum = sum(nums[:index])
        right_sum = sum(nums[index+1:])
        if left_sum == right_sum:
            return index
    return -1


print(pivotIndex(1, [1, 7, 3, 6, 5, 6]))
