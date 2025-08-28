from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # space: O(1)
        # time: O(log n)
        
        index = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            if nums[index] < target:
                left = index + 1
            elif nums[index] > target:
                right = index - 1
            elif nums[index] == target:
                return index
        
        return -1
