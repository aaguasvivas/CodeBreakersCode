def sumSubarrays(arr, target):
    # O(n) time O(1) space
    out = 0
    total_sum = 0
    start = -1

    for i in range(len(arr)):
        total_sum += arr[i]

        while total_sum > target:
            start += 1
            total_sum -= arr[start]
        out += i - start
    return out


nums = [1, 2, 3, 0, 3]
target = 3
