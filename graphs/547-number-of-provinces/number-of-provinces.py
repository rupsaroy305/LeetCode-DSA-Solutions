class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        
        def dfs(city):
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and next_city not in visited:
                    visited.add(next_city)
                    dfs(next_city)
        
        provinces = 0
        
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1
        
        return provinces