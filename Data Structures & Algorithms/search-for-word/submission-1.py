class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        n=len(word)
        vis=[[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(r,c,i):
            if i==n:
                return True
            
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or vis[r][c]):
                return False
            
            vis[r][c]=True
            res=(backtrack(r+1,c,i+1) or
                 backtrack(r-1,c,i+1) or
                 backtrack(r,c+1,i+1) or 
                 backtrack(r,c-1,i+1))
            vis[r][c]=False

            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        
        return False




        