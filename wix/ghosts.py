from collections import deque
from typing import List


def can_win_ghosts(target: List[int], ghosts: List[List[int]]):
    grid = make_matrix(50)
    player_road = shortest_path(grid, (0, 0), tuple(target))
    for ghost in ghosts:
        ghost_start = tuple(ghost)
        if (player_road >= shortest_path(grid, ghost_start, tuple(target))):
            return False
    return True


def shortest_path(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    tr, tc = target

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False]*cols for _ in range(rows)]
    parent = {}

    queue = deque()
    queue.append((sr, sc, 0))
    visited[sr][sc] = True

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (tr, tc):

            return dist

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                not visited[nr][nc] and
                grid[nr][nc] == 0
            ):
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

    return -1, []


def make_matrix(n, fill=0):
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(fill)
        mat.append(row)
    return mat


ghosts = [[1, 0], [0, 3]]
target = [0, 1]
print(can_win_ghosts(target, ghosts))
