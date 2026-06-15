from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc, time + 1))
        
        if fresh != 0:
            return -1
        
        return minutes