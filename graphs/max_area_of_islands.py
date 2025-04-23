from collections import deque
from typing import List


def maxAreaOfIsland(grpah: List[List[str]]) -> int:
    size_of_max_island = 0
    visted = set()
    for r in range(len(grpah)):
        for c in range(len(grpah[0])):
            if ((r, c)not in visted and grpah[r][c] == 1):
                currnet_island_size = bfs(r, c, grpah, visted)
                if currnet_island_size > size_of_max_island:
                    size_of_max_island = currnet_island_size
    return size_of_max_island


def bfs(row, col, graph, visited) -> int:
    size = 0
    q = deque()
    q.append((row, col))
    while (q):
        r, c = q.popleft()
        possible_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for row_dir, col_dir in possible_dir:
            nr = r + row_dir
            nc = c + col_dir
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and (nr, nc) not in visited:
                if graph[nr][nc] == 1:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    size += 1
    return size


grid = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]
print(maxAreaOfIsland(grid))

# by ido rabin
