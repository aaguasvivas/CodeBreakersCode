class MaxPriorityQueue:
    def __init__(self):
        self.arr = [None]

    def insert(self, key):
        self.arr.append(key)
        self.swim()

    def swim(self):
        idx = len(self.arr) - 1
        while idx // 2 > 0 and self.arr[idx // 2] < self.arr[idx]:
            self.arr[idx], self.arr[idx //
                                    2] = self.arr[idx // 2], self.arr[idx]
            idx = idx // 2

    def get_max(self):
        assert not self.isEmpty()
        return self.arr[1]

    def delMax(self):
        assert not self.isEmpty()
        self.arr[1], self.arr[len(self.arr) -
                              1] = self.arr[len(self.arr) - 1], self.arr[1]
        val = self.pop()
        self.sink()
        return val

    def sink(self):
        idx = 1
        while idx * 2 < len(self.arr):
            cur = self.arr[idx]
            left = self.arr[idx * 2]
            right = float('-inf')
            if idx * 2 + 1 < len(self.arr):
                right = self.arr[idx * 2 + 1]
            if cur >= left and cur >= right:
                return
            if left > right:
                self.arr[idx], self.arr[idx *
                                        2] = self.arr[idx * 2], self.arr[idx]
                idx = idx * 2
            else:
                self.arr[idx], self.arr[idx * 2 +
                                        1] = self.arr[idx * 2 + 1], self.arr[idx]
                idx = idx * 2 + 1

    def isEmpty(self):
        return len(self.arr) == 1

    def size(self):
        return len(self.arr) - 2


def heapSort(arr):
    pq = MaxPriorityQueue()

    for item in arr:
        pq.insert(item)

    idx = len(arr) - 1

    while not pq.isEmpty():
        arr[idx] = pq.delMax()
        idx -= 1
