def maxMin(lst):
    result = []
    # Iterate half list because we are appending twice
    for i in range(len(lst) // 2):
        # Append corresponding last element
        result.append(lst[-(i + 1)])
        # Append current element
        result.append(lst[i])
    if len(lst) % 2:
        # If there is a middle value that was not appended, then append/add to the end
        result.append(lst[len(lst) // 2])

    return result


# Time Complexity: O(n)
