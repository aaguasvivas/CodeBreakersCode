def non_greedy_max_sum(nums):
    max_sum = float("-inf")
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            max_sum = max(max_sum, nums[i]+nums[j])
    return max_sum


def greedy_max_sum(nums):
    largest_2_nums = []
    for num in nums:
        largest_2_nums.append(num)
        largest_2_nums.sort(reverse=True)
        if len(largest_2_nums) > 2:
            largest_2_nums.pop()
    return largest_2_nums[0] + largest_2_nums[1]
