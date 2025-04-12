from typing import List


def solve(temperatures: List[int]) -> List[int]:
    results = []
    stack = []
    result_dict = {i: -1 for i in range(len(temperatures))}

    for index, temperature in enumerate(temperatures):
        if len(stack) == 0:
            stack.append((temperature, index))
        else:
            while stack and temperature > stack[-1][0]:
                item_to_be_updated = stack.pop()
                result_dict[item_to_be_updated[1]] = index - \
                    item_to_be_updated[1]
            stack.append((temperature, index))

    for i in range(len(temperatures)):
        value = result_dict[i]
        if value == -1:
            results.append(0)
        else:
            results.append(value)

    return results


temperatures = [73, 100, 75, 71, 69, 72, 76, 73]
print(solve(temperatures))

# by ido rabin
