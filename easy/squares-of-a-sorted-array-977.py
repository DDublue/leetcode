from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # space: O(n)
        # time: O(n)

        # square nums so we can sort easier
        nums = [num**2 for num in nums]
        squares = [0] * len(nums)

        # compare values at left and right index of nums
        squares_ptr = len(nums) - 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] > nums[right]: # left is larger
                squares[squares_ptr] = nums[left]
                left += 1
            else: # right is equal/larger
                squares[squares_ptr] = nums[right]
                right -= 1
            squares_ptr -= 1

        return squares
