# O(logn) time and O(1) space
def searchRotatedArray(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid

        # Case 1, arr[low] > arr[mid], meaning we have a pivot
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Case 2, arr[lo] < arr[mid], no pivot, perform normal binary search
        else:
            if target > arr[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# O(n) time and O(1) space
def searchRotatedArrayWithDups(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid

        while lo != mid and arr[mid] == arr[lo]:
            lo += 1
        # Case 1, arr[low] > arr[mid], meaning we have a pivot
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Case 2, arr[lo] < arr[mid], no pivot, perform normal binary search
        else:
            if target > arr[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    rot_arr = [13, 15, 17, 19, 1, 3, 5, 7, 9, 11]

    for i in range(1, 20):
        print(i, ":", searchRotatedArray(arr, i),
              "|", searchRotatedArray(rot_arr, i))

    dup_arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2]
    target = 4
    print(searchRotatedArrayWithDups(dup_arr, target))
