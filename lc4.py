class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            char_value = ord(columnTitle[len(columnTitle) - 1 - i]) - ord('A') + 1
            result += char_value * (26 ** i)
        return result
