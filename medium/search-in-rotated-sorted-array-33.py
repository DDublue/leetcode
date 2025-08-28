from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # space: O(1)
        # time: O(log n)

        # Find the pivot
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # Binary search on shifted list
        gap = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            realmid = (mid + gap) % len(nums)
            if nums[realmid] == target:
                return realmid

            if nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
