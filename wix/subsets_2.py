class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        self.solve(nums, result, [], 0)
        return result

    def solve(self, nums, result, acc, index):
        if index >= len(nums):
            sorted_acc = sorted(acc)
            if sorted_acc not in result:
                result.append(sorted_acc)
            return

        acc.append(nums[index])
        self.solve(nums, result, acc, index + 1)

        acc.pop()
        self.solve(nums, result, acc, index + 1)


nums = [4, 4, 4, 1, 4]
sol = Solution()
print(sol.subsetsWithDup(nums))
