class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtrack(i,subs):
            if i==len(nums):
                res.append(subs.copy())
                return
            
            subs.append(nums[i])
            backtrack(i+1,subs)
            subs.pop()

            backtrack(i+1,subs)
        
        backtrack(0,[])
        return res
