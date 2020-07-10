def findMinimum_by_Addy(arr):
    if len(arr) <= 0:
        return None
    min_value = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            i += 1
        else:
            i += 1
    return min_value


def findMinimum(arr):
    if len(arr) <= 0:
        return None
    minimum = arr[0]
    # At every index compare its value with minimum and if it's less
    # then make that index value new minimum value
    for val in arr:
        if val < minimum:
            minimum = val
    return minimum
