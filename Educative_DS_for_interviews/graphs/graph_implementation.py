from Graph import Graph
from Stack import MyStack


class Node(object):
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


class myStack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return self.size() == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()


class myQueue:
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return len(self.queueList) == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front


class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

        # If we were to impement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph")
        print
        for i in range(self.vertices):
            print("|", i, end=" | =>")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")


def bfs_traversal_helper(g, source, visited):
    result = ""
    # Create Queue for Breadth First Traversal
    # and enqueue source in it
    queue = myQueue()
    queue.enqueue(source)
    visited[source] = True  # Mark as visited
    # Traverse while queue is not empty
    while queue.isEmpty() is False:
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head
        while temp is not None:
            if visited[temp.data] is False:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current node
            temp = temp.next
    return result, visited


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # Visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result


def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create stack and push source in it
    stack = myStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while stack.isEmpty() is False:
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].head
        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next
    return result, visited


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # Visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices

    # rec_node_stack keeps track of the nodes which are a part of
    # the current recursive call
    rec_node_stack = [False] * g.vertices

    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True
    return False


def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in the recursion stack. Cycle found
    if rec_node_stack[node]:
        return True

    # It has been visited before this recursion
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True

    head_node = g.array[node].head
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next

    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False


def find_mother_vertex(g):
    # Traverse the Graph array and perform DFS operation on each vertex
    # The vertex whose DFS traversal results equal to the total number
    # of vertices in graph is a mother vertex
    num_of_vertices_reached = 0
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if num_of_vertices_reached is g.vertices:
            return i
        return - 1

# Performs DFS traversal on graph starting from source
# Returns total number of vertices which can be reached from source


def perform_DFS(g, source):
    num_of_vertices = g.vertices
    vertices_reached = 0  # To store how many vertices reached from source
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you push it into stack
    visited = [False] * num_of_vertices

    # Create a stack for DFS and push source in it
    stack = myStack()
    stack.push(source)
    visited[source] = True

    # Traverse while stack is not empty
    while stack.is_empty() is False:
        # Pop a vertex/node from stack
        current_node = stack.pop()
        # Get adjacent vertices to the current_node from the list,
        # and if only push unvisited adjacent vertices into stack
        temp = g.array[current_node].head
        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next
    return vertices_reached + 1  # +1 to include the source itself


# We only need Graph and Stack for this question!


def find_mother_vertex_last_finished_vertex(g):
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.vertices)

    # To store last finished vertex (or mother vertex)
    last_v = 0

    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if visited[i] is False:
            perform_DFS(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False]*(g.vertices)
    perform_DFS(g, last_v, visited)
    if any(i is False for i in visited):
        return -1
    else:
        return last_v


# A recursive function to print DFS starting from v
def perform_DFS_LFV(g, node, visited):

    # Mark the current node as visited and print it
    visited[node] = True

    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].head_node
    while(temp):
        if visited[temp.data] is False:
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element


def num_edges(g):
    return sum(g.array[i].length() for i in range(g.vertices)) // 2


def check_path(g, source, dest):
    # BFS to check path between source and dest
    # Keep track of visited vertices
    visited = [False]*(g.vertices)

    # Create a queue for BFS
    queue = MyQueue()

    # Enque source and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Loop to traverse the whole graph using BFS
    while not(queue.is_empty()):

        node = queue.dequeue()

        # Check if dequeued node is the destination
        if node is dest:
            return True

        # Continue BFS by obtaining first element in linked list
        adjacent = g.array[node].head_node
        while adjacent:
            # enqueue adjacent node if it has not been visited
            if visited[adjacent.data] is False:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element

    # Destination was not found in the search
    return False


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1) is True:
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if visited[i] is False:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node) is True:
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True
        adjacent = adjacent.next_element

    return False


def find_min(g, a, b):
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True
    # Traverse while queue is not empty
    while (not queue.is_empty()):
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (not visited[temp.data]) or (temp.data is b):
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1


def remove_edge(graph, source, dest):
    # If empty graph
    if(len(graph.array) is 0):
        return graph
    # check if source valid
    if(source >= len(graph.array) or source < 0):
        return graph
    # check if dest valid
    if(dest >= len(graph.array) or dest < 0):
        return graph
    # Delete by calling delete on head of LinkedList
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph
