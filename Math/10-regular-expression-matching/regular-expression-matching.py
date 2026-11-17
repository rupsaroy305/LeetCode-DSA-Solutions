class Solution:
    def isMatch(self, s, p):
        memo={}
        def check(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(p):
                return i==len(s)
            first=i<len(s) and (s[i]==p[j] or p[j]=='.')
            if j+1<len(p) and p[j+1]=='*':
                result=check(i,j+2) or (first and check(i+1,j))
            else:
                result=first and check(i+1,j+1)
            memo[(i,j)]=result
            return result
        return check(0,0)