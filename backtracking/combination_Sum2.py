def solve(numbers: list, target: int):
    numbers.sort()
    result = []

    def backtracking(index: int, current_array: list, desire_target: int):
        if desire_target == 0:
            result.append(current_array.copy())
            return
        if desire_target < 0:
            return

        prev = -1
        for i in range(index, len(numbers)):
            if numbers[i] == prev:
                continue
            current_array.append(numbers[i])
            backtracking(i + 1, current_array, desire_target - numbers[i])
            current_array.pop()
            prev = numbers[i]

    backtracking(0, [], target)
    return result
