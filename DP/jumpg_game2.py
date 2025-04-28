from typing import List


def min_jump(jumps: List[int]) -> int:
    step = 0
    memo = {}
    return solve(0, jumps, memo)


def solve(index: int, jumps: List[int], memo):
    if index in memo:
        return memo[index]
    if index >= len(jumps)-1:
        return 0
    if 
    result = []
    for j in range(index+1, index+jumps[index]+1):
        result.append(solve(j, jumps, memo)+1)
    memo[index] = min(result)
    return memo[index]


nums = [2, 3, 0, 1, 4]
print(min_jump(nums))
