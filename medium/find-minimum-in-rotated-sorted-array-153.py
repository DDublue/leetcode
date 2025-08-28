from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # space: O(1)
        # time: O(log n)

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Compare adjacent numbers for inflection
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # No inflection, so search left or right depending on last element vs. mid
            if nums[-1] > nums[mid]:
                right = mid - 1
            elif nums[-1] < nums[mid]:
                left = mid + 1

        return -5001
