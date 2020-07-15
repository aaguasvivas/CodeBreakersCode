from LinkedList import LinkedList


def reverseLinkedList(head):
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


lst = LinkedList()
for i in range(10):
    lst.insertFront(i)
print(lst)
lst = reverseLinkedList(lst)
print(lst)
