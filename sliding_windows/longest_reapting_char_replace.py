def char_replace(s: str, k: int) -> int:
    res = 0
    l = 0
    char = {}
    for right_pointer in range(len(s)):
        char[s[right_pointer]] = 1 + char.get(s[right_pointer], 1)
        if (right_pointer-l+1 - max(char.values) > k):
            char[s[l]] -= 1
            l += 1
        res = max(res, right_pointer-l+1)
    return res

    # by ido rabin
