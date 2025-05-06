"""1048. Longest String Chain
Medium
Topics
Companies
Hint
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words."""


from typing import List


def longest_word_chain(words: List[str], word):
    memo = {}

    def dfs(word, best):
        if word in memo:
            return memo[word]

        for index, ch in enumerate(word):
            test_word = word[:index]+word[index+1:]
            if (test_word in words):
                current = 1+dfs(test_word, best)
                if current > best:
                    best = current
        memo[word] = best
        return best
    return dfs(word, 1)


words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
words = sorted(words, key=len, reverse=True)
print(words)
print(longest_word_chain(words, words[0]))
print(max(longest_word_chain(words, w) for w in words))
