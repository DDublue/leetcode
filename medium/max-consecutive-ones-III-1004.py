from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # space: O(1)
        # time: O(n)

        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
                    