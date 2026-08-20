class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """ans = []
        solve = []
        for i in range(0, len(nums) + 1):
            ans.append(i)
        for j in range(len(nums)):
            if nums[j] == ans[j]:
                ans[j] = 0
        for k in range(len(ans)):
            if k != 0:
                solve.append(k)
        return solve
        """
        n = len(nums)
        nums2 = []
        set1 = set(nums)
        for i in range(1, n+1):
            nums2.append(i)
        set2 = set(nums2)
        res = set2 - set1
        return list(res)