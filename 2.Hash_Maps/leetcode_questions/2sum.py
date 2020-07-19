class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            potential = target - nums[i]
            if potential in result:
                return [result[potential], i]
            else:
                result[nums[i]] = i
        return []
