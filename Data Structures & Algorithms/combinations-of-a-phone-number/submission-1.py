class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        digitToChar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz"
        }

        res=[""]

        for digit in digits:
            tmp=[]
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr+c)
                
            res=tmp
        return res
        
        # TC-> O(n*4^n) because we create 4^n combinations, and each takes O(n)
        # SC-> O(n) recursion, O(n*4^n) for the o/p list

        