class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node, leaves):
            if not node:
                return
            
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            
            dfs(node.left, leaves)
            dfs(node.right, leaves)
        
        leaves1 = []
        leaves2 = []
        
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        
        return leaves1 == leaves2