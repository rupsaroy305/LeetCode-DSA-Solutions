class Solution:
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            good = 1 if node.val >= max_so_far else 0
            
            new_max = max(max_so_far, node.val)
            
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            
            return good
        
        return dfs(root, root.val)