def isValid(s: str) -> bool:
    stack = []
    openers = ['(', '{', '[']
    closers = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in s:
        if char in openers:
            stack.append(char)
        else:
            matching = stack.pop()
            if not (closers[char] == matching):
                return False
    return True


s = "[(])"
print(isValid(s))
# by ido rabin
