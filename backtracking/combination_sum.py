def solve(numbers: list, target: int):
    result = []

    def backtracking(index: int, current_array: list, desire_target: int):
        if desire_target == 0:
            result.append(current_array.copy())
            return
        if index >= len(numbers) or desire_target < 0:
            return

        current_array.append(numbers[index])
        backtracking(index, current_array, desire_target - numbers[index])
        current_array.pop()
        backtracking(index + 1, current_array, desire_target)

    backtracking(0, [], target)
    return result


print(solve([10,1,2,7,6,1,5], 8))

# by ido rabin
