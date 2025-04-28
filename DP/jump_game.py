
from typing import List


def canJump(jumps: List[int]):
    memo = {}
    return solve(0, jumps, memo)


def solve(index: int, jumps: List[int], memo: dict):
    if index in memo:
        return memo[index]
    elif index >= len(jumps)-1:
        return True
    elif jumps[index] == 0:
        return False
    else:
        for j in range(index+1, index+jumps[index]+1):
            if (solve(j, jumps, memo)):
                memo[index] = True
                return True
        memo[index] = False
        return False


nums = [1, 2, 0, 1, 0]

print(jump_game(nums))
