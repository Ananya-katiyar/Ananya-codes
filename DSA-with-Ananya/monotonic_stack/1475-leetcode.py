class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        ans = prices[:]
        for i in range(n):
            curr = prices[i]
            while stack and curr <= prices[stack[-1]]:
                prev = stack.pop()
                ans[prev] -= curr
            stack.append(i)
        return ans