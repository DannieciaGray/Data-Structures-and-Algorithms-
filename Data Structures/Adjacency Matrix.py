from collections import deque

def course_schedule(n, prerequisites):
    # Step 1: Build adjacency matrix and in-degree list
    adj_matrix = [[0] * n for _ in range(n)]
    in_degree = [0] * n

    for dest, src in prerequisites:
        if adj_matrix[src][dest] == 0:
            adj_matrix[src][dest] = 1
            in_degree[dest] += 1

    # Step 2: Enqueue all courses with no prerequisites (in-degree 0)
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    # Step 3: Process the queue
    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in range(n):
            if adj_matrix[course][neighbor]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # Step 4: Check if all courses are included
    return order if len(order) == n else []
