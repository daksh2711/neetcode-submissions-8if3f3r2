
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            if n < 0:
                curMax, curMin = curMin, curMax

            curMax = max(n, n * curMax)
            curMin = min(n, n * curMin)

            res = max(res, curMax)

        return res
