class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[0]*len(nums)
        prod=1
        zero_ck=0

        for num in nums:

            if num!=0:
                prod*=num
            
            if num==0:
                zero_ck+=1
        
        if zero_ck>1:
            return res
        
        for i,num in enumerate(nums):

            if num==0:
                res[i]=prod
            
            elif zero_ck==0:

                res[i]=prod//num
        
        return res
        


        