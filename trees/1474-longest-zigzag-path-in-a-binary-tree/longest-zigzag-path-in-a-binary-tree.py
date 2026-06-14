class Solution:
    def longestZigZag(self, root):
        self.ans = 0
        
        def dfs(node, direction, length):
            if not node:
                return
            
            self.ans = max(self.ans, length)
            
            if direction == "L":
                dfs(node.left, "L", 1)
                dfs(node.right, "R", length + 1)
            else:
                dfs(node.right, "R", 1)
                dfs(node.left, "L", length + 1)
        
        dfs(root.left, "L", 1)
        dfs(root.right, "R", 1)
        
        return self.ans