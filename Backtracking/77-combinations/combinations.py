class Solution:
    def combine(self, n, k):
        result=[]
        def backtrack(start, combo):
            if len(combo)==k:
                result.append(combo[:])
                return
            for i in range(start,n+1):
                combo.append(i)
                backtrack(i+1,combo)
                combo.pop()
        backtrack(1,[])
        return result