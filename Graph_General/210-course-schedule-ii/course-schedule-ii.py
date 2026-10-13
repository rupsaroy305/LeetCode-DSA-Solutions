from collections import defaultdict,deque
class Solution:
    def findOrder(self,numCourses,prerequisites):
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            course=q.popleft()
            ans.append(course)
            for nextCourse in graph[course]:
                indegree[nextCourse]-=1

                if indegree[nextCourse]==0:
                    q.append(nextCourse)
        return ans if len(ans)==numCourses else []