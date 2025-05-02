class Solution(object):
    def originalDigits(self, s):
        numbers_dict = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
        }

        result = ""
        for key in sorted(numbers_dict, key=int):
            value = numbers_dict[key]
            if self.check_if_digit_exists(value, s):
                result += key
        return result

    def check_if_digit_exists(self, digit, word):
        for char in digit:
            if char not in word:
                return False
        return True


s = "ninefour"
sol = Solution()
print(sol.originalDigits(s))
