class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def backtrack(i,curList,total):
            if total==target:
                res.append(curList.copy())
                return
            
            if i>=len(nums) or total>target:
                return
            
            curList.append(nums[i])
            backtrack(i,curList,total+nums[i])
            curList.pop()
            backtrack(i+1,curList,total)
        
        backtrack(0,[],0)
        return res
            
            
        