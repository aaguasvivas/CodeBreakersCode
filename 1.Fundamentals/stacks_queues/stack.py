class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.first_item = None
        self._size = 0

    # prints out stack in order
    def __str__(self):
        # O(n) time
        # O(n) space
        cur = self.first_item
        out = ""

        while cur:
            out += str(cur.val) + "|"
            cur = cur.next
        return out

    def push(self, item):
        # O(1) time and space
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1

    def pop(self):
        # O(1) time and space
        if self.isEmpty():
            return

        old_first_item = self.first_item
        self.first_item = self.first_item.next
        self._size -= 1
        return old_first_item.val

    def isEmpty(self):
        # O(1) time and space
        return self.size() == 0

    def size(self):
        # O(1) time and space
        return self._size


if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        stack.push(i)

    print(stack)

    for _ in range(3):
        print(stack.pop())

    for i in range(5, 10):
        stack.push(i)

    print(stack)
