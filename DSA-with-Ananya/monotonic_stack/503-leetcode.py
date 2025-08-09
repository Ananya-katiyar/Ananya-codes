class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mapping = {}
        stack = []
        for i in range (2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                prev = stack.pop()
                mapping[prev] = curr
            if i < n:
                stack.append(i)
        while stack:
            mapping[stack.pop()] = -1        
        res = []
        for i in range(n):
            res.append(mapping[i])
        return res