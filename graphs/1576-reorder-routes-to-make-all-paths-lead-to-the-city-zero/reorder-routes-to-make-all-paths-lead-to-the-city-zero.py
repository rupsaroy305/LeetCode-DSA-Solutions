class Solution:
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]
        
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        
        visited = set()
        stack = [0]
        changes = 0
        
        while stack:
            city = stack.pop()
            visited.add(city)
            
            for nxt, cost in graph[city]:
                if nxt not in visited:
                    changes += cost
                    stack.append(nxt)
        
        return changes