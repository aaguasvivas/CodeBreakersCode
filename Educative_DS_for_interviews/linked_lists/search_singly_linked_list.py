from Node import Node
from LinkedList import LinkedList

# Start from the head node
# Traverse the list till you either find a node with the
# given value or you reach the end node which will indicate that
# the given node does not exist in the list


def search_addy(lst, value):
    new_node = Node(value)
    curr = lst.get_head()

    if curr.data == new_node.data:
        return True

    while curr.next:
        curr = curr.next
        if cur.data == new_node.data:
            return True
    if curr.next is None:
        return False


def search(lst, value):

    # Start from first element
    curr = lst.get_head()

    # Traverse the list till you reach the end
    while curr:
        if curr.data is value:
            return True  # Value found
        curr = curr.next
    return False  # Value not found


def search_recursive(node, value):
    # Base case, if node is None, return False
    if not node:
        return False
    # Check if node's data matches our value
    if node.data is value:
        return True

    # Recursive call to next node in the list
    return search_recursive(node.next, value)
