class Solution:
    def sumNumbers(self, root):        
        def dfs(node, current_sum):
            if node is None:
                return 0            
            current_sum = current_sum * 10 +node.val            
            if node.left is None and node.right is None:
                return current_sum    
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        return dfs(root, 0)