from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.solve(0, memo, cost), self.solve(1, memo, cost))

    def solve(self, n, memo, const):  # <-- only added self here
        if n in memo:
            return memo[n]
        if n >= len(const):
            return 0

        memo[n] = const[n] + \
            min((self.solve(n + 1, memo, const), self.solve(n + 2, memo, const)))
        return memo[n]
