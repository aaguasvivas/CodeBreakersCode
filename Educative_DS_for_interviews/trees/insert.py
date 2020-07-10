class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        current = self
        parent = None

        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild
        if parent is None:
            parent = Node(val)
        elif val < parent.val:
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def insert_recursive(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return
