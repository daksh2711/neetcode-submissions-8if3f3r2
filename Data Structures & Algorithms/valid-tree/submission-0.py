class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj=[[] for _ in range(n)]
        
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        vis=set()

        def dfs(node,parent):

            vis.add(node)

            for nei in adj[node]:
                if nei==parent:
                    continue

                if nei in vis:
                    return False
                
                if not dfs(nei,node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(vis)==n
        