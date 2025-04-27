from typing import List
from collections import deque


def islandsAndTreasure(graph: List[List[int]]):
    result_matrix = [
        [-2, -2, -2, -2],
        [-2, -2, -2, -2],
        [-2, -2, -2, -2],
        [-2, -2, -2, -2]
    ]
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] < 0:
                result_matrix[row][col] = graph[row][col]
            else:
                result_matrix[row][col] = bfs(row, col, graph)

    return result_matrix


def bfs(start_row, start_col, graph) -> int:
    if graph[start_row][start_col] == 0:
        return 0

    visited = set()
    q = deque()
    q.append((start_row, start_col, 0))  # row, col, distance

    while q:
        row, col, dist = q.popleft()

        if (row, col) in visited:
            continue
        
        visited.add((row, col))

        if graph[row][col] == 0:
            return dist

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                if graph[nr][nc] != -1:
                    q.append((nr, nc, dist + 1))


    return 2147483647


mat = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]


print(solve(mat))

# by einav and ido
