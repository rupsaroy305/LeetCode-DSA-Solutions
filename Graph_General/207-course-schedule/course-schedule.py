from collections import defaultdict,deque
class Solution:
    def canFinish(self,numCourses,prerequisites):
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            course=q.popleft()
            count+=1
            for nextCourse in graph[course]:
                indegree[nextCourse]-=1
                if indegree[nextCourse]==0:
                    q.append(nextCourse)
        return count==numCourses