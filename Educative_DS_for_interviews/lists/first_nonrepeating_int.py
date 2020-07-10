def findFirstUnique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i], 0)
    counts = counts.fromkeys(lst, 0)
    for ele in lst:
        counts[ele] += 1  # Incrementing for every repetition
    for ele in lst:
        if counts[ele] <= 1:
            return ele
    return None

# Time Complexity: O(n)
# Space Complexity: O(n)
