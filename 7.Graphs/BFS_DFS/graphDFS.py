def DFS(adj_list, source, target):
    visited = set()
    return DFS(adj_list, source, target, visited)


# O(n^2) time and O(n) space
def _DFS(adj_list, cur_node, target, visited):
    if cur_node == target:
        return True

    if cur_node in visited:
        return False
    visited.add(cur_node)
    for neighbor in adj_list[cur_node]:
        if _DFS(adj_list, neighbor, target, visited):
            return True
    return False
