from collections import deque
class Solution:
    def zigzagLevelOrder(self,root):
        if not root:
            return []
        q=deque([root])
        ans=[]
        reverse=False
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                level.reverse()
            ans.append(level)
            reverse=not reverse
        return ans