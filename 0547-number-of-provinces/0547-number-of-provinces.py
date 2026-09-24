class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        prov=0
        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not visited[neighbour] :
                    visited[neighbour]=True
                    dfs(neighbour)
        for city in range(n):
            if not visited[city]:
                visited[city]=True
                dfs(city)
                prov +=1
        return prov
            