class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for symbol in s:
            current_value = roman_values[symbol]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Example usage:
solution = Solution()

roman1 = "III"
print(solution.romanToInt(roman1))  # Output: 3

roman2 = "LVIII"
print(solution.romanToInt(roman2))  # Output: 58

roman3 = "MCMXCIV"
print(solution.romanToInt(roman3))  # Output: 1994
