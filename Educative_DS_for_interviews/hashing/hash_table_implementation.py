import collections


class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6
    # Helper Functions

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        # Find the node with the given key
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            print(key, "-", value, "inserted at index:", b_index)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key is key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    print(key, "-", value, "inserted at index:", b_index)
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None
    # Remove a value based on a key

    def delete(self, key):
        # Find index
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If key exists at first slot
        if head.key is key:
            self.bucket[b_index] = head.nxt
            print(key, "-", head.value, "deleted")
            # Decrease the size by one
            self.size -= 1
            return self
        # Find the key in slots
        prev = None
        while head is not None:
            # If key exists
            if head.key is key:
                prev.nxt = head.nxt
                print(key, "-", head.value, "deleted")
                # Decrease the size by one
                self.size -= 1
                return
            # Else keep moving in chain
            prev = head
            head = head.nxt

        # If key does not exist
        print("Key not found")
        return


def is_subset(list1, list2):
    s = set(list1)

    for elem in list2:
        if elem not in s:
            return False
    return True


def is_disjoint(list1, list2):
    s = set(list1)  # Create set of list1 elements
    # iterate list 2
    for elem in list2:
        # if element in list1 then return False
        if elem in s:
            return False
    # Return True if no common element
    return True


def find_symmetric(my_list):
    # Create an empty set
    pair_set = set()
    result = []
    # Traverse through the given list
    for pair in my_list:
        # Make a tuple and a reverse tuple out of the pair
        pair_tup = tuple(pair)
        pair.reverse()
        reverse_tup = tuple(pair)
        # Check if the reverse tuple exists in the set
        if(reverse_tup in pair_set):
            # Symmetric pair found
            result.append(list(pair_tup))
            result.append(list(reverse_tup))
        else:
            # Insert the current tuple into the set
            pair_set.add(pair_tup)
    return result


def trace_path(my_dict):
    result = []
    # Create a reverse dict of the given dict i.e if the given dict has (N,C)
    # then reverse dict will have (C,N) as key-value pair
    # Traverse original dict and see if it's key exists in reverse dict
    # If it doesn't exist then we found our starting point.
    # After the starting point is found, simply trace the complete path
    # from the original dict.
    reverse_dict = dict()
    # To fill reverse dict, iterate through the given dict
    keys = my_dict.keys()
    for key in keys:
        reverse_dict[my_dict.get(key)] = key
    # Find the starting point of itinerary
    from_loc = None
    keys_rev = reverse_dict.keys()
    for key in keys:
        if key not in reverse_dict:
            from_loc = key
            break
            # Trace complete path
    to = my_dict.get(from_loc)
    while to is not None:
        result.append([from_loc, to])
        from_loc = to
        to = my_dict.get(to)
    return result


def find_pair(my_list):
    result = []
    # Create Has my_dict with Key being added and value being a pair
    # i.e key = 3 , value = {1,2}
    # Traverse all possible pairs in my_list and store sums in map
    # If sum already exist then print out the two pairs.
    my_dict = dict()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            added = my_list[i] + my_list[j]  # calculate sum
            # the 'in' operator on dict() item has a. complexity of O(1)
            # This is because of hashing
            # On a list, the 'in' operator would have the complexity of O(n)
            if added not in my_dict:
                # If added is not present in dict then insert it with pair
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                # added already present in Map
                prev_pair = my_dict.get(added)
                # Since list elements are distinct, we don't
                # need to check if any element is common among pairs
                second_pair = [my_list[i], my_list[j]]
                result.append(prev_pair)
                result.append(second_pair)
                return result
    return result


def find_sub_zero(my_list):
    # Use hash table to store the cumulative sum as key
    # and the element as value till which sum has been calculated
    # Traverse the list and return true if either
    # elem == 0 or sum == 0 or hash table already contains the sum
    # If you completely traverse the list
    # and haven't found any of the above three
    # conditions then simply return false
    ht = dict()
    total_sum = 0
    # Traverse through the given list
    for elem in my_list:
        total_sum += elem
        if elem is 0 or total_sum is 0 or ht.get(total_sum) is not None:
            return True
        ht[total_sum] = elem
    return False


def is_formation_possible(lst, word):

    if len(word) < 2 or len(lst) < 2:
        return False

    hash_table = HashTable()
    for elem in lst:
        hash_table.insert(elem, True)

    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        if hash_table.search(first) is not None:
            check1 = True
        if hash_table.search(second) is not None:
            check2 = True

        # Return True If both substrings are present in the trie
        if check1 and check2:
            return True

    return False


def findFirstUnique(lst):
    orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    orderedCounts = orderedCounts.fromkeys(lst, 0)
    for ele in lst:
        orderedCounts[ele] += 1  # Incrementing for every repitition
    for ele in orderedCounts:
        if orderedCounts[ele] == 1:
            return ele
    return None


def detect_loop(lst):
    # Used to store nodes which we already visited
    visited_nodes = set()
    current_node = lst.get_head()

    # Traverse the set and put each node in the visitedNodes set
    # and if a node appears twice in the map
    # then it means there is a loop in the set
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)  # Insert node in visitedNodes set
        current_node = current_node.next_element
    return False


def remove_duplicates(lst):
    current_node = lst.get_head()
    prev_node = lst.get_head()
    # To store values of nodes which we already visited
    visited_nodes = set()
    # If List is not empty and there is more than 1 element in List
    if not lst.is_empty() and current_node.next_element:
        while current_node:
            value = current_node.data
            if value in visited_nodes:
                # current_node is already in the HashSet
                # connect prev_node with current_node's next element
                # to remove it
                prev_node.next_element = current_node.next_element
                current_node = current_node.next_element
                continue
            # Visiting currentNode for first time
            visited_nodes.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next_element


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    unique_values = set()
    result = LinkedList()

    start = list1.get_head()

    # Traverse the first list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element

    start = list2.get_head()

    # Traverse the second list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element

    # Add elements of unique_vales to result
    for x in unique_values:
        result.insert_at_head(x)
    return result
