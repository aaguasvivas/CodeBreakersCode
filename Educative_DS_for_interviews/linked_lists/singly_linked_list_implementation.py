class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        return self.head

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, "-> None")
        return True


list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(1, 10):
    list.insert_at_head(i)
list.print_list()
