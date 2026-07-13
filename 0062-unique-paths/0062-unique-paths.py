class Solution:
    def solve (self, m: int, n:int, memo) -> list:
        if m==1 or n==1:
            return 1
        if memo[m][n] != -1:
            return memo[m][n]
        if m==0 or n==0:
            return 0
        memo[m][n] = self.solve(m-1, n, memo) + self.solve(m, n-1, memo)
        return memo[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]* (n+1) for i in range(m+1)]
        return self.solve(m, n, memo)
