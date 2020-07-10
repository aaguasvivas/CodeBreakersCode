from Node import Node
from LinkedList import LinkedList


def delete_at_head(lst):
    # Get head anf firstElement of list
    first_element = lst.get_head()

    # if List is not empty then link head
    # to the nextElement of firstElement
    if first_element is not None:
        lst.head = first_element.next
        first_element.next = None
    return


def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is empty")
        return deleted

    curr = lst.get_head()  # Get current node
    prev = None  # Get previous node

    if curr.data is value:
        lst.delete_at_head()  # Use previous function
        deleted = True
        return deleted

    while curr is not None:
        if value is curr.data:
            # previous node now points to next node
            previous.next = curr.next
            curr.next = None
            deleted = True
            break
        prev = curr
        curr = curr.next
    if deleted is False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted")

    return deleted


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()
