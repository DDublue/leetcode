from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # time: O(n^2)
        # space: O(n)

        trapped_water = 0
        n = len(height)
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        # get max left's and right's of each height to subtract from
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
            
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # At each height, it uses the minimum height of its left and right maxes, similar to the max container question.
        # Water can only fill upto its min wall at a particular height, taking into account extra height at the spot itself.
        for i, h in enumerate(height):
            filled_water_amount = min(max_left[i], max_right[i]) - h
            if filled_water_amount > 0:
                trapped_water += filled_water_amount

        return trapped_water
