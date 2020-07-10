from Node import Node
from LinkedList import LinkedList


def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head = new_node
        return

    curr = lst.get_head()

    while curr.next:
        curr = curr.next

    curr.next = new_node
    return
