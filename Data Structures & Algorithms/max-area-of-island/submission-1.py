class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis=set()
        area=0
        rows,cols=len(grid),len(grid[0])
        ans=0
        def dfs(r,c,vis):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            
            if (r,c) in vis:
                return 0
            
            if grid[r][c]==0:
                return 0
            
            vis.add((r,c))

            return (1+dfs(r+1,c,vis)+
            +dfs(r-1,c,vis)
            +dfs(r,c+1,vis)
            +dfs(r,c-1,vis) )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in vis:
                    area=max(area,dfs(r,c,vis))
                
        
        return area

        
        