class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # Total size of the English alphabet
        self.is_end_word = False  # true if node represents the end of the word
        self.char = char

    # Function to mark the currentNode as Lead
    def mark_as_leaf(self):
        self.is_end_word = True

    # Function to unmark the currentNode as Leaf
    def unmark_as_leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Function to get the index of a character 't'
    def get_index(self, t):
        return ord(t) - ord('a')
        # ord(): Given a string of length one,
        # returns an integer representing the unicode code of the char

    # Function to insert a key in the Trie
    def insert(self, key):
        # None keys are not allowed
        if key is None:
            return

        key = key.lower()  # keys are stored in lowercase
        current_node = self.root
        index = 0  # To store the character index

        # Iterate the trie with the given character index,
        # If the index points to None
        # simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current_node = current_node.children[index]

        current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False

        key = key.lower()
        current_node = self.root
        index = 0

        # Iterate the Trie with given character index,
        # If it is None at any point then we stop and return False
        # We will return true only if we reach leftNode and have traversed the
        # Trie based on the length of the key

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node is not None and current_node.is_end_word:
            return True
        return False

    # Helper Function to return true if current_node does not have any children

    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True

    # Recursive function to delete given key
    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if current_node is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # If we have reached at the node
        # which points to the alphabet at the end of the key.
        if level is length:
            # If there are no nodes ahead of this node in this path
            # Then we can delete this node
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True

            # If there are nodes ahead of current_node in this path
            # Then we cannot delete current_node. We simply unmark this as leaf
            else:
                current_node.unMarkAsLeaf()
                deleted_self = False

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            if child_deleted:
                # Making children pointer also None: since child is deleted
                current_node.children[self.get_index(key[level])] = None
                # If current_node is leaf node then
                # current_node is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current_node.is_end_word:
                    deleted_self = False

                # If child_node is deleted and current_node has more children
                # then current_node must be part of another key
                # So, we cannot delete currenNode
                elif self.has_no_children(current_node) is False:
                    deleted_self = False

                # Else we can delete current_node
                else:
                    current_node = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return

        self.delete_helper(key, self.root, len(key), 0)


def total_words(root):
    result = 0

    # Leaf denotes end of a word
    if root.is_end_word:
        result += 1

    for i in range(26):
        # Check if the node has children
        if root.children[i] is not None:
            # Recursively return the word count
            result += total_words(root.children[i])
    return result


def get_words(root, result, level, word):

    # Leaf denotes end of word
    if root.is_end_word:
        # Current word is stored till the level in char array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Non None child, so add that index to the char array
            word[level] = chr(i + ord('a'))  # Add char for the level
            get_words(root.children[i], result, level + 1, word)


def find_words(root):
    result = []
    word = [None] * 20  # Assuming max level is 20
    get_words(root, result, 0, word)
    return result

# Challenge 3: List Sort Using Trie


def get_words(root, result, level, word):
    # Leaf denote end of a word
    if root.is_end_word:
        # current word is stored till the level in the char array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if root.children[i] is not None:
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(arr):
    result = []
    trie = Trie()

    for x in range(len(arr)):
        trie.insert(arr[x])

    word = [''] * 20
    get_words(trie.get_root(), result, 0, word)
    return result


def is_formation_possible(dct, word):

    trie = Trie()
    # Create Trie and insert dictionary elements in it
    for x in range(len(dct)):
        trie.insert(dct[x])
    # Get root
    current_node = trie.root

    # Iterate all the letters of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])

        # if the prefix of word does not exist, word would not either
        if current_node.children[char] is None:
            return False

        # if substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return True
        elif current_node.children[char].is_end_word:
            if trie.search(word[i+1:]):
                return True

        current_node = current_node.children[char]
    return False
