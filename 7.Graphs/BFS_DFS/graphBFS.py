from Queue import Queue


# O(n^2) runtime and O(n) space
def bfs(adj_list, source, target):
    Q = Queue()
    Q.put(source)
    seen = set(source)

    while not Q.empty():
        cur = Q.get()
        if cur == target:
            return True
        for neighbor in adj_list[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.put(neighbor)
    return False
