class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        current = self

        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def search(self, val):
        current = self
        while current is not None:
            if val < current.val:
                current = current.leftChild

            elif val > current.val:
                current = current.rightChild

            else:
                return True
        return False
