class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 1:
            return N

        i = 1
        j = 1

        while i < N:
            if nums[i] != nums[i - 1]:  # Unique element found
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

# [0,1,2,3,4,2,2,3,3,4]
#                    i
#            j
