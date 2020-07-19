class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        # O(1) time and space
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    # Return True if deque is empty, else False
    def isEmpty(self):
        # O(1) time and space
        return self.getSize() == 0

    # Return number of items in the deque
    def getSize(self):
        # O(1) time and space
        return self.size

    # Insert item to the front of the deque
    def addFirst(self, item):
        # O(1) time and space
        new_node = ListNode(item)
        prev_first = self.head.next
        # update head.next.prev
        self.head.next.prev = new_node
        # update head.next
        self.head.next = new_node
        # update new nodes next and prev
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1

    # Insert item to the end of the deque
    def addLast(self, item):
        # O(1) time and space
        new_node = ListNode(item)
        prev_last = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        new_node.next = self.tail
        new_node.prev = prev_last

        self.size += 1

    # Delete and return the item at the front of the deque
    def removeFirst(self):
        # O(1) time and space
        if self.isEmpty():
            print("Trying to remove from empty list")
            return
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1

    def removeLast(self):
        # O(1) time and space
        if self.isEmpty():
            print("Trying to remove from empty list")
            return
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

    def asList(self):
        # O(n) time and space
        lst = []

        curr = self.head.next

        while curr.next:
            lst.append(curr.val)
            curr = curr.next
        return lst


if __name__ == "__main__":
    dq = Deque()
    for i in range(1, 6):
        dq.addFirst(i)

    for i in range(6, 11):
        dq.addLast(i)
    print(dq.asList())
    dq.removeFirst()
    print(dq.asList())
    dq.removeLast()
    print(dq.asList())
