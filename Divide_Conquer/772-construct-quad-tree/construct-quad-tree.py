class Solution:
    def construct(self, grid):
        n = len(grid)
        def build(row, col, size):
            value = grid[row][col]
            same = True
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != value:
                        same = False
                        break
                if not same:
                    break
            if same:
                return Node(value == 1, True)
            half = size // 2
            root = Node(True, False)
            root.topLeft = build(row, col, half)
            root.topRight = build(row, col + half, half)
            root.bottomLeft = build(row + half, col, half)
            root.bottomRight = build(row + half, col + half, half)
            return root
        return build(0, 0, n)