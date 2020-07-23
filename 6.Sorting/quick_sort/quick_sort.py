# O(n^2) worst case time O(logn) space


def quickSort(arr):
    _quickSort(arr, 0, len(arr) - 1)


def _quickSort(arr, lo, hi):
    if lo >= hi:
        return
    pivot = partition(arr, lo, hi)

    # partition bottom
    _quickSort(arr, lo, pivot - 1)
    # partition top
    _quickSort(arr, pivot + 1, hi)


def partition(arr, lo, hi):
    # returns the index of our pivot element
    # everything with index < index of pivor is < pivot
    pivot = arr[lo]
    swap_index = lo + 1

    for i in range(lo + 1, hi + 1):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    arr[lo], arr[swap_index - 1] = arr[swap_index - 1], arr[lo]
    return swap_index - 1


if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 5, 8, 4, 3, 2, 1, 14, 13]
    quickSort(arr)
    print(arr)
