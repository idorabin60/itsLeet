from typing import List
from collections import deque, Counter, defaultdict


def orangesRotting(graph: List[List[int]]):
    result_matrix = [[2000000 for _ in range(len(graph[0]))]
                     for _ in range(len(graph))]
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 2:
                result_matrix[row][col] = 0
                bfs(row, col, graph, result_matrix)
    max_minute = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 1:
                if result_matrix[row][col] > max_minute:
                    max_minute = result_matrix[row][col]
    return max_minute if max_minute != 2000000 else -1


def bfs(row, col, graph, result_matrix):
    visited = set()
    queue = deque()
    queue.append((row, col, 0))  # minute it became root
    while queue:
        row, col, dist = queue.popleft()
        if (row, col) in visited:
            continue
        else:
            visited.add((row, col))
            if result_matrix[row][col] > dist:
                result_matrix[row][col] = dist
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                    if graph[nr][nc] == 1:
                        queue.append((nr, nc, dist+1))


grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
print(orangesRotting(grid))
