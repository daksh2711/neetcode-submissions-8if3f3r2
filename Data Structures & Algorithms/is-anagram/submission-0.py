class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1={}
        count2={}
        

        for ch in s:
            count1[ch]=count1.get(ch,0)+1
        
        for ch in t:
            count2[ch]=count2.get(ch,0)+1
        if count1==count2:
            return True
        
        return False
        