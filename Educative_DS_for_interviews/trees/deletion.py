from BST_implementation import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False

    def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)


class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
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

    def search(self, val):
        if val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self, val):
        # if current node's val is less than that of root node,
        # then only search in left subtree otherwise right subtree
        if val < self.val:
            if(self.leftChild):
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        elif val > self.val:
            if(self.rightChild):
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            # deleting node with right child
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            # deleting node with left child
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while(current.leftChild is not None):
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self


def preOrderPrint(node):
    if node is not None:
        print(node.val)
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)


def postOrderPrint(node):
    if node is not None:
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val)


def inOrderPrint(node):
    if node is not None:
        postOrderPrint(node.leftChild)
        print(node.val)
        postOrderPrint(node.rightChild)


def findMin_iterative(root):
    if root is None:
        return None
    while root.leftChild:
        root = root.leftChild
    return root.val


def findMin_recursive(root):
    if root is None:
        return None
    elif root.leftChild is None:
        return root.val
    else:
        return findMin_recursive(root.leftChild)


def findKthMax(root, k):
    if k < 1:
        return None
    node = findKthMax_recursive(root, k)  # get the node at kth position
    if node is not None:
        return node.val
    return None


counter = 0
current_max = None


def findKthMax_recursive(root, k):
    global counter
    global current_max

    if root is None:
        return None

    # recurse to right for max node
    node = findKthMax_recursive(root.rightChild, k)
    if counter is not k and root.val is not current_max:
        # Increment counter if kth element is not found
        counter += 1
        current_max = root.val
        node = root
    elif current_max is None:
        # Increment counter if kth element is not found
        # and there is no current_max set
        counter += 1
        current_max = root.val
        node = root
    # base condition reached as kth largest is found
    if counter == k:
        return node
    else:
        return findKthMax_recursive(root.leftChild, k)


def findAncestors(root, k):
    if not root:
        return None
    ancestors = []
    current = root

    while current is not None:
        if k > current.val:
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:
            ancestors.append(current.val)
            current = current.leftChild
        else:
            return ancestors[::-1]
    return []


def findHeight(root):
    if root is None:
        return -1
    else:
        max_sub_tree_height = max(findHeight(
            root.leftChild), findHeight(root.rightChild))
        return 1 + max_sub_tree_height


def findKNodes(root, k):
    res = []
    findK(root, k, res)
    return str(res)


def findK(root, k, res):
    if root is None:
        return
    if k == 0:
        res.append(root.val)
    else:
        findK(root.leftChild, k - 1, res)
        findK(root.rightChild, k - 1, res)
