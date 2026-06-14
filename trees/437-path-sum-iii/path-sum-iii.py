class Solution:
    def pathSum(self, root, targetSum):
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            count = 1 if curr_sum == targetSum else 0
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            return count
        
        if not root:
            return 0
        
        # paths starting from root + from left subtree + right subtree
        return (
            dfs(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )