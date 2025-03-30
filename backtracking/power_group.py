def solve(group: list):
    result = []
    current_itration_set = []

    def backtracking(i):
        if i >= len(group):
            result.append(current_itration_set.copy())
            return
        current_itration_set.append(group[i])
        backtracking(i+1)
        current_itration_set.pop()
        backtracking(i+1)
    backtracking(0)
    return result


print(solve([1, 2, 3]))
# by ido rabin
