# Case 1: Where node to delete has no children (just delete)
# Case 2: Where node has one child (replace node with its one child)

# O(n) worst case time O(logn) usually
# O(1) space


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        pass

    def deleteRecursive(self, val):
        self.root = self._deleteRecursive(val, self.root)

    def _deleteRecursive(self, val, curNode):
        if curNode is None:
            return None

        if curNode.val < val:
            curNode.right = self._deleteRecursive(val, curNode.right)

        elif curNode.val > val:
            curNode.left = self._deleteRecursive(val, curNode.left)

        else:
            if not curNode.left and not curNode.right:
                return None

            elif curNode.left and curNode.right:
                smallest = self.getSmallestAndDelete(curNode.right, curNode)

                smallest.left = curNode.left
                smallest.right = curNode.right
                return smallest
            else:
                if curNode.left:
                    return curNode.left
                else:
                    return curNode.right
        return curNode

    def getSmallestAndDelete(self, curNode, prev):
        while curNode.left:
            prev = curNode
            curNode = curNode.left
        if prev.left is curNode:
            prev.left = curNode.right
        else:
            prev.right = curNode.right
        return curNode
