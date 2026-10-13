class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        vis=[False]*n
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if not vis[nei]:
                    vis[nei]=True
                    dfs(nei)

        res=0

        for node in range(n):
            if not vis[node]:
                dfs(node)
                res+=1

        return res              