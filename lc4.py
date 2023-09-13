class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            char_value = ord(columnTitle[len(columnTitle) - 1 - i]) - ord('A') + 1
            result += char_value * (26 ** i)
        return result

solution = Solution()
print(solution.titleToNumber("A"))  # Output: 1
print(solution.titleToNumber("AB"))  # Output: 28
print(solution.titleToNumber("ZY"))  # Output: 701