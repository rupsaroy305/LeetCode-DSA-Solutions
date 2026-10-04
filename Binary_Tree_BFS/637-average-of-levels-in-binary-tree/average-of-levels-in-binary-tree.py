from collections import deque
class Solution:
    def averageOfLevels(self,root):
        q=deque([root])
        ans=[]
        while q:
            total=0
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                total+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(total/n)
        return ans