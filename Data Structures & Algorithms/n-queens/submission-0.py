class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for i in range(n)]

        def backtrack(r):
            # Reach the last row, append all rows to res
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            
            # Check if each row is safe, then place Q and backtrack
            for c in range(n):
                if self.isSafe(r,c,board):
                    board[r][c]='Q'
                    backtrack(r+1)
                    board[r][c]='.'
                
        backtrack(0)
        return res

    def isSafe(self,r,c,board):
        # 1. Check directly above
        row=r-1
        while row>=0:
            if board[row][c]=='Q':
                return False
            row-=1
            
        # 2. Check in upper left diagonal
        row,col=r-1,c-1
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
            
        # 3. Check in upper right diagonal
        row,col=r-1,c+1
        while row>=0 and col<len(board):
            if board[row][col]=='Q':
                return False
            row-=1
            col+=1
        return True

            

        