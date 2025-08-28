from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # space: O(1)
        # time: O(n)

        left = 0
        min_size = 10000000000
        total = 0

        # Sliding window; expand if next number can still fit sum, else shrink from left if over target
        for right, num in enumerate(nums):
            total += num
            if total < target:
                continue
            else:
                while total >= target and left < right:
                    min_size = min(min_size, right - left + 1)
                    total -= nums[left]
                    left += 1
            
            if total >= target:
                min_size = min(min_size, right - left + 1)

        return min_size if min_size < 10000000000 else 0
