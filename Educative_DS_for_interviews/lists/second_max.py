def findSecondMaximum(lst):
    if len(lst) < 2:
        return None
    current_max = float('-inf')
    prev_max = float('-inf')

    for ele in lst:
        if ele > current_max:
            prev_max = current_max
            current_max = ele
        elif ele > prev_max:
            prev_max = ele
    return prev_max


# Time Complexity: O(n)

print(findSecondMaximum([1, 2, 2, 3, 4, 4, 4, 4, 5]))
