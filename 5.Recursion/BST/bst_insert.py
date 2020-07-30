class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Worst case O(n) time and O(1) space
class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return binaryTreeToStr(self.root)

    def insertIterative(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            prev = None
            isLeft = None
            cur = self.root

            while cur:
                prev = cur
                if cur.val > val:
                    isLeft = True
                    cur = cur.left
                else:
                    isLeft = False
                    cur = cur.right
            if isLeft:
                prev.left = Node(val)
            else:
                prev.right = Node(val)

    def insertRecursive(self, val):
        self.root = self._insertRecursive(self, val, self.root)

    def _insertRecursive(self, val, curNode):
        if not curNode:
            return Node(val)
        if curNode.val > val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        return curNode
