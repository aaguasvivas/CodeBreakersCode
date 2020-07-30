class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return binaryTreeToStr(self.root)

    # O(n) worst case time, O(1) space
    def getIterative(self, val):
        cur = self.root

        while cur:
            if cur.val == val:
                return True
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def getRecursive(self, val):
        return self._getRecursive(val, self.root)

    def _getRecursive(self, val, curNode):
        if not curNode:
            return False
        if curNode.val == val:
            return True
        elif curNode.val > val:
            return self._getRecursive(val, curNode.left)
        else:
            return self._getRecursive(val, curNode.right)
