from collections import deque
class Solution:
    def snakesAndLadders(self,board):
        n=len(board)
        q=deque([(1,0)])
        seen={1}
        while q:
            curr,moves=q.popleft()
            if curr==n*n:
                return moves
            for nxt in range(curr+1,min(curr+6,n*n)+1):
                r=(n-1)-(nxt-1)//n
                c=(nxt-1)%n
                if (n-1-r)%2:
                    c=n-1-c
                dest=board[r][c]
                if dest!=-1:
                    nxt=dest
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt,moves+1))
        return -1