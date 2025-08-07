class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                prev= stack.pop()
                mapping[prev] = curr 
            stack.append(curr)
        while stack:
            mapping [stack.pop()] = -1
        res = []
        for i in nums1:
            res.append(mapping[i])
        return res