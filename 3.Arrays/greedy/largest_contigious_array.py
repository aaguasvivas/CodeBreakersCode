"""Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

Example:
  Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
  Output: 6
  Explanation: [4, -1, 2, 1] has the largest sum = 6. """

# Python program to find maximum contiguous subarray
# Code snippet from GeeksForFeeks.

# Function to find the maximum contiguous subarray
from sys import maxint


def maxSubArraySum(a, size):

    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))
