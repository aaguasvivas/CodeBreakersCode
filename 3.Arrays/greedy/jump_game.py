def canJump(nums):
    # O(n) time O(1) space
    best_index = 0
    for i in range(len(nums)):
        if i > best_index:
            return False
        best_index = max(best_index, nums[i] + i)
    return True


nums = [2, 3, 1, 1, 4]
