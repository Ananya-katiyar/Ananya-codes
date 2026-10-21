class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        yes = 0
        no = 0
        for i in range(n):
            next_yes = nums[i] + no
            next_no = max(yes, no)
            yes = next_yes
            no = next_no
        return (max(yes, no))