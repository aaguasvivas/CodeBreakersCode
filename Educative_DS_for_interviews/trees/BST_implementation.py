class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)
