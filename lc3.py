from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# Example usage:
solution = Solution()

nums1 = [1, 1, 2]
result1 = solution.removeDuplicates(nums1)  # Output: 2, nums1 = [1, 2, ...]
print(result1)  # Print the number of unique elements
print(nums1[:result1])  # Print the modified nums list with unique elements

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = solution.removeDuplicates(nums2)  # Output: 5, nums2 = [0, 1, 2, 3, 4, ...]
print(result2)  # Print the number of unique elements
print(nums2[:result2])  # Print the modified nums list with unique elements
