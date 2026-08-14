class Solution:
    def merge(self,intervals):
        intervals.sort()
        ans=[]
        for a,b in intervals:
            if not ans or a>ans[-1][1]:
                ans.append([a,b])
            else:
                ans[-1][1]=max(ans[-1][1],b)
        return ans