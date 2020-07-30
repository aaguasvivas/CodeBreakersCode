def detect_cycle(adj_list):
    visited = set()
    for key in adj_list.keys():
        if key not in visited:
            if DFS(key, set(), visited, adj_list):
                return True
    return False


def DFS(cur_node, cur_path, visited, adj_list):
    cur_path.add(cur_node)
    for neighbor in adj_list[cur_node]:
        if cur_node == neighbor:
            continue
        if cur_node in cur_path:
            return True
        if neighbor not in visited and DFS(neighbor, cur_path, visited, adj_list):
            return True
    cur_path.remove(cur_node)
    return False
