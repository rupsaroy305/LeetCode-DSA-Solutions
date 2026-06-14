from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        
        max_sum = float('-inf')
        best_level = 1
        level = 1
        
        while q:
            level_size = len(q)
            curr_sum = 0
            
            for _ in range(level_size):
                node = q.popleft()
                curr_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_level = level
            
            level += 1
        
        return best_level
