class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]
            
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for nxt, value in graph[start]:
                if nxt not in visited:
                    result = dfs(nxt, end, visited)
                    
                    if result != -1.0:
                        return value * result
            
            return -1.0
        
        answer = []
    
        for c, d in queries:
            answer.append(dfs(c, d, set()))
        
        return answer