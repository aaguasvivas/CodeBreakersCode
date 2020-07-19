def containerMostWater(arr):
    # O(n) time O(1) space
    if len(arr) < 2:
        return -1
    start = 0
    end = len(arr) - 1
    max_product = float('-inf')

    while start < end:
        product = min(arr[start], arr[end]) * (end - start)
        max_product = max(max_product, product)

        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1

    return max_product


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# expected output: 49
print(containerMostWater(arr))
