from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # space: O(1)
        # time: O(log n)

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return middle + 1 if target >= nums[middle] else middle
