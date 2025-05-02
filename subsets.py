from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    solve(nums, result, [], 0)
    return result


def solve(nums: List[int], result: List[List[int]], acc: List[int], index: int):
    if index >= (len(nums)):
        if acc not in result:
            result.append(acc.copy())
        return
    acc.append(nums[index])
    solve(nums, result, acc, index+1)
    acc.pop()
    solve(nums, result, acc, index+1)


nums = [1, 2, 2]
print(subsets(nums))
