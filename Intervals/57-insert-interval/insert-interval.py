class Solution:
    def insert(self,intervals,newInterval):
        ans=[]
        s,e=newInterval
        i=0
        while i<len(intervals) and intervals[i][1]<s:
            ans.append(intervals[i])
            i+=1
        while i<len(intervals) and intervals[i][0]<=e:
            s=min(s,intervals[i][0])
            e=max(e,intervals[i][1])
            i+=1
        ans.append([s,e])
        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans