class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        vis=set()
        rows,cols=len(grid),len(grid[0])

        def dfs(r,c,vis):

            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            
            if (r,c) in vis:
                return 
            
            if grid[r][c]=='0':
                return 
            
            vis.add((r,c))

            dfs(r+1,c,vis)
            dfs(r-1,c,vis)
            dfs(r,c+1,vis)
            dfs(r,c-1,vis)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in vis:
                    dfs(r,c,vis)
                    ans+=1
        
        return ans

            
        