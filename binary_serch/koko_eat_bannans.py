import math
from typing import List


def check_if_ratio_valid(ratio: int, h: int, piles: List):
    sum = 0
    for bannans in piles:
        sum = sum + math.ceil(bannans/ratio)
    return sum < h


def koko_eat_bannas(h: int, piles: List):
    left_pointer = 1
    right_pointer = max(piles)
    smallest_valid = right_pointer
    while left_pointer <= right_pointer:
        midiean = (left_pointer + right_pointer) // 2
        if check_if_ratio_valid(midiean, h, piles):
            smallest_valid = midiean
            right_pointer = midiean - 1
        else:
            left_pointer = midiean + 1
    return smallest_valid


piles = [1, 4, 3, 2]
h = 9

print(koko_eat_bannas(h, piles))
