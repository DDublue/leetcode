from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # space: O(n)
        # time: O(n)

        # if target - num in hist, return index of target-num and num
        hist = dict()
        for i, num in enumerate(nums):
            hist[target - num] = i

        for i, num in enumerate(nums):
            if num in hist and i != hist[num]:
                return [i, hist[num]]
