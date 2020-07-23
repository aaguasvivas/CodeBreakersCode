def selectionSort(arr):
    # O(n^2) time and O(1) space
    for i in range(len(arr)):
        min_number = arr[i]
        swap_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_number:
                min_number = arr[j]
                swap_index = j
        arr[i], arr[swap_index] = arr[swap_index], arr[i]


if __name__ == '__main__':
    arr = [10, 6, 8, 4, 5, 1, 3, 7, 9, 2]

    selectionSort(arr)
    print(arr)
