class Node:
    def __init__(self, data):
        self.data = data
        self.previous_element = None
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None


def length(lst):
    # start from first element
    curr = lst.get_head()
    count = 0

    # traverse list and count number of nodes
    while curr:
        count += 1
        curr = curr.next()
    return count


def reverse(lst):
    # To reverse linked list, we need to keep track of three things
    previous = None
    current = lst.get_head()
    next = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

        lst.head = previous
    return lst


# Floyd's Cycle Finding Algorithm

def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()

    while onestep and twostep and twostep.next:
        onestep = onestep.next  # Move one node at a time
        twostep = twostep.next.next  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False


def find_mid(lst):
    if lst.is_empty():
        return -1
    current_node = lst.get_head()
    if current_node.next_element is None:
        # Only 1 element exist in array so return its value
        return current_node.data

    mid_node = current_node
    current_node = current_node.next_element.next_element

    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of list

    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data

    return -1


def remove_duplicates(lst):
    if lst.is_empty():
        return None

    # If list only has one node, leave it unchanged
    if lst.get_head().next_element is None:
        return lst

    outer_node = lst.get_head()
    while outer_node:
        inner_node = outer_node  # Iterator for the inner loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    # Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element

            else:
                # Otherwise simply iterate ahead
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element
    return lst


def union(list1, list2):
    # Return other List if one of them is empty
    if list1.is_empty():
        return elements(list2)
    elif list2.is_empty():
        return elements(list1)

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of the second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1


def intersection(list1, list2):
    result = LinkedList()
    visited = set()  # Keep track of all the visited nodes
    current_node = list1.get_head()

    # Traversing list1 and adding all unique nodes into the hash set
    while current_node:
        value = current_node.data
        if value not in visited:
            visited.add(value)  # Visiting current_node for the first time
        current_node = current_node.next_element

    start = list2.get_head()

    # Traversing list 2
    # Nodes which are already present in visited_nodes are added to result
    while start:
        value = start.data
        if value in visited:
            result.insert_at_head(start.data)
        start = start.next_element
    result.remove_duplicates()
    return result


def find_nth(lst, n):
    if lst.is_empty():
        return -1

    # Find Length of list
    length = 0
    current_node = lst.get_head()

    while current_node.next_element:
        current_node = current_node.next_element
        length += 1

    # Find node which is at (len - n + 1) position from start
    current_node = lst.get_head()
    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data

    return -1


def find_nth_two_pointers(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    if not lst.is_empty():
        while count < n:
            if end_node is None:
                return -1
            end_node = end_node.next_element
            count += 1

    while end_node is not None:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    return nth_node.data
