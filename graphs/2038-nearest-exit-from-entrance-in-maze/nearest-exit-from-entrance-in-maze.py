from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        rows = len(maze)
        cols = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))

        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()

            moves = [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]

            for nr, nc in moves:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if maze[nr][nc] == '+':
                    continue

                if (nr, nc) in visited:
                    continue

                if nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1:
                    return steps + 1

                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

        return -1