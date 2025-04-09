def dfs(graph, start):
    visited = set()
    result = []

    def dfs_helper(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs_helper(neighbor)

    dfs_helper(start)
    return result


def bfs(graph, start):
    from collections import deque
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result
