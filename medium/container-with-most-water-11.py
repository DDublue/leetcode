from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # time: O(n)
        # space: O(1)

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right]) # height limited by shorter line
            max_water = max(max_water, width * min_height) # max area
            
            # Moves shorter line to find a taller line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1


        return max_water
