class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self._size = 0
        self.head = Node("dummy")
        self.tail = self.head

    def enqueue(self, item):
        # O(1) time and space
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1

    def dequeue(self):
        # O(1) time and space
        if self.isEmpty():
            return "Removing from empty queue"
        out = self.head.next
        self.head.next = self.head.next.next
        self._size -= 1
        if self.isEmpty():
            self.tail = self.head
        return out.item

    def isEmpty(self):
        # O(1) time and space
        return self.size() == 0

    def size(self):
        # O(1) time and space
        return self._size

    def items(self):
        # O(n) time and space
        out = []
        curr = self.head.next
        while curr:
            out.append(curr.item)
            curr = curr.next
        return out


if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    for i in range(3):
        queue.enqueue(i)
    print(queue.items())
    print("Now removing items...")
    for _ in range(4):
        print(queue.dequeue())

    for i in range(2, 4):
        queue.enqueue(i)
    print(queue.items())
