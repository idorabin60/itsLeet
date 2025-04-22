from collections import deque, Counter, defaultdict
from typing import List


def bfs(row, col, graph, visited):
    q = deque()
    q.append((row, col))
    while (q):
        r, c = q.popleft()
        possible_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for row_dir, col_dir in possible_dir:
            if (r+row_dir) < len(graph) and c+col_dir < len(graph[0]) and (r+row_dir, c+col_dir) not in visited and graph[r+row_dir][c+col_dir] == '1':
                q.append((r+row_dir, c+col_dir))
                visited.add((r+row_dir, c+col_dir))


def numIslands(matrix: List[List[str]]) -> int:
    number_of_islands = 0
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if ((i, j) not in visited) and matrix[i][j] == "1":
                bfs(i, j, matrix, visited)
                number_of_islands = number_of_islands+1
    return number_of_islands


grid = [
    ["0", "1", "1", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid))
