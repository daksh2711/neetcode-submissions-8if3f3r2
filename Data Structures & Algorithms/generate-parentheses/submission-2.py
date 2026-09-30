class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(curStr,op,close):
            if op==n and close==n:
                res.append(curStr)
                return
            
            if op<n:
                backtrack(curStr+'(',op+1,close)
            if close<op:
                backtrack(curStr+')',op,close+1)
            
        
        backtrack("",0,0)

        return res
            
        