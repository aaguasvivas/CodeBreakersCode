def binarySearch(nums):
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo
