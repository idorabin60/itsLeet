from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.solve(0, nums, memo) 

    def solve(self, index, nums, memo):
        if index in memo:
            return memo[index]
        if index >= len(nums):
            return 0
        memo[index] = max(self.solve(index + 2, nums, memo) + nums[index],
                          self.solve(index + 1, nums, memo))
        return memo[index]
