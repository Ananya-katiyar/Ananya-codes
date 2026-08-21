class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        lp = 1
        rp = 1
        ans = float('-inf')
        for i in range(len(nums)):
            if lp == 0:
                lp = 1
            if rp == 0:
                rp = 1
            lp = lp * nums[i]
            rp = rp * nums[n - i - 1]
            maxval = max(lp, rp)
            ans = max(ans, maxval)
        return ans