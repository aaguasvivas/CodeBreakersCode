class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            potential = target - nums[i]

            if potential in res:
                return [res[potential], i]
            else:
                res[nums[i]] = i
        return []
