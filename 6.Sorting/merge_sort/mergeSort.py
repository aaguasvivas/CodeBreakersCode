# O(nlogn) time O(n) space
def mergeSort(arr):
    _mergeSort(arr, 0, len(arr) - 1)


def _mergeSort(arr, lo, hi):
    # O(logn) time and O(1) space
    # Takes care of dividing the array into parts
    if lo >= hi:
        return
    mid = (lo + hi) // 2 + 1
    # divide lower halp
    _mergeSort(arr, lo, mid - 1)
    # divides upper half
    _mergeSort(arr, mid, hi)
    # merge everything
    _merge(arr, lo, mid, hi)


def _merge(arr, start_1, start_2, end_2):
    # O(n) time and space
    # merges the parts together
    copy = arr[:]
    cur = start_1
    p1 = start_1
    p2 = start_2

    while cur <= end_2:
        if p1 < start_2 and p2 <= end_2:
            if copy[p1] < copy[p2]:
                arr[cur] = copy[p1]
                p1 += 1
            else:
                arr[cur] = copy[p2]
                p2 += 1
        elif p1 < start_2:
            arr[cur] = copy[p1]
            p1 += 1
        else:
            arr[cur] = copy[p2]
            p2 += 1
        cur += 1


if __name__ == '__main__':
    arr = [8, 4, 3, 9, 10, 2, 1, 5, 6, 7]
    mergeSort(arr)
    print(arr)
