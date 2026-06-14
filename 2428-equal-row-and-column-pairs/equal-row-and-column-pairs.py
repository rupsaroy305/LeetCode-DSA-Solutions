class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        
        row_count = {}
        
        # store all rows
        for row in grid:
            t = tuple(row)
            row_count[t] = row_count.get(t, 0) + 1
        
        result = 0
        
        # check columns
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_count:
                result += row_count[col_tuple]
        
        return result