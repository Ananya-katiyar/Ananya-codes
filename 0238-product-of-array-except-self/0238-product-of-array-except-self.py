class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        zeros = nums.count(0)
        idx = 0
        prod = 1
        if zeros >= 2:
            return [0] * n
        elif zeros == 1:
            for i in range(n):
                if nums[i] == 0:
                    idx = i
                    continue
                prod *= nums[i]
            ans = [0] * n
            ans[idx] = prod
            return ans
        else:
            product = 1
            for i in range(n):
                product *= nums[i]
            prod1 = [product] * n
            for i in range(n):
                prod1[i] //= nums[i]
            return prod1
