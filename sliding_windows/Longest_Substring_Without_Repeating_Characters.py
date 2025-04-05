def lengthOfLongestSubstring(s: str) -> int:
    max_substring_len = 0
    currnet_len = 0
    left_pointer = 0
    char_set = set()
    for right_pointer, character in enumerate(s):
        while character in char_set:
            char_set.remove(s[left_pointer])
            left_pointer = left_pointer+1
        char_set.add(character)
        if max_substring_len < right_pointer-left_pointer + 1:
            max_substring_len = right_pointer-left_pointer + 1
    return max_substring_len


s = "zxyzxyz"
print(lengthOfLongestSubstring(s))
