class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        
        def bfs(r,c):
            visit=[[False]*COLS for _ in range(ROWS)]
            visit[r][c]=True
            steps=0
            q=deque([(r,c)])

            while q:
                for _ in range(len(q)):
                    row,col=q.popleft()

                    if grid[row][col]==0:
                        return steps
                    
                    for nr,nc in directions:
                        dr,dc=row+nr,col+nc

                        if (0<=dr<ROWS and 0<=dc<COLS and not visit[dr][dc] and grid[dr][dc]!=-1):
                            visit[dr][dc]=True
                            q.append((dr,dc))
                steps+=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==INF:
                    grid[r][c]=bfs(r,c)                    