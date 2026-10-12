from collections import defaultdict,deque
class Solution:
    def calcEquation(self,equations,values,queries):
        graph=defaultdict(list)
        for (a,b),v in zip(equations,values):
            graph[a].append((b,v))
            graph[b].append((a,1/v))
        def bfs(start,end):
            if start not in graph or end not in graph:
                return -1.0
            if start==end:
                return 1.0
            q=deque([(start,1.0)])
            seen={start}
            while q:
                node,value=q.popleft()
                for neighbor,weight in graph[node]:
                    if neighbor==end:
                        return value*weight
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append((neighbor,value*weight))
            return -1.0
        return [bfs(a,b) for a,b in queries]