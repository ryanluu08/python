from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_indices:
                return [num_indices[complement], i]

            # If not, add the current number to the dictionary
            num_indices[num] = i

        # If no solution is found, return an empty list or handle the error as needed
        return []

# Example usage:
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]

