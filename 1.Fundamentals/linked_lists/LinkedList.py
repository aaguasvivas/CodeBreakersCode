class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node("dummy")
        self._size = 0

    def __str__(self):
        # O(n) runtime
        # O(n) space
        out = ""
        cur = self.head.next

        while cur:
            out += str(cur.item) + "|"
            cur = cur.next

        return out

    def insertFront(self, item):
        # O(1) runtime
        # O(1) space
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        self._size += 1

    def insertLast(self, item):
        # O(n) runtime
        # O(1) space
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    def removeBeginning(self):
        # O(1) runtime
        # O(1) space
        assert(self.size() > 0)
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        # O(1) runtime
        # O(1) space
        return self._size

    def reverseLinkedList(self):
        curr = self.head.next
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head.next = prev


if __name__ == '__main__':
    # test cases
    linked_list = LinkedList()

    for i in range(1, 6):
        linked_list.insertFront(i)

    print(linked_list)

    linked_list.removeBeginning()
    linked_list.removeBeginning()

    print(linked_list)

    for i in range(6, 11):
        linked_list.insertLast(i)

    print(linked_list)

    # reverse
    linked_list.reverseLinkedList()
    print(linked_list)

    linkedList = LinkedList()
    print(linkedList)
    linkedList.reverseLinkedList()
    print(linkedList)

    linkedList.insertFront(1)
    print(linkedList)
    linkedList.reverseLinkedList()
    print(linkedList)
