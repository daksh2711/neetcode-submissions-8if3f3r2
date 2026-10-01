class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        check=[False]*len(nums)

        def backtrack(cur):

            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            
            for j in range(0,len(nums)):
                if check[j]==False:
                    cur.append(nums[j])
                    check[j]=True
                    backtrack(cur)
                    check[j]=False
                    cur.pop()
                
        backtrack([])
        return res

            

            
        