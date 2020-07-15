# Source GeeksForGeeks

# Merges two subarrays of a_list[].
# First subarray is a_list[l..m]
# Second subarray is a_list[m+1..r]


def merge(a_list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = a_list[l + i]

    for j in range(0, n2):
        R[j] = a_list[m + 1 + j]

    # Merge the temp arrays back into a_list[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a_list[k] = L[i]
            i += 1
        else:
            a_list[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        a_list[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        a_list[k] = R[j]
        j += 1
        k += 1

# Recursive mergesort (Top Down)
# l is for left index and r is right index of the
# sub-array of a_list to be sorted


def mergesortTopDown(a_list, l, r):
    if l < r:

        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2

        # Recursive call to sort first and second halves
        mergesortTopDown(a_list, l, m)
        mergesortTopDown(a_list, m+1, r)
        merge(a_list, l, m, r)
