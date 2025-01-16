from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space: O(n)
        # time: O(n)
        answer = [1] * len(nums)
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        
        # uses previous prefix for each i to reduce computations
        # ...and can safely multiply to answer[i]
        for i in range(1, len(nums)):
            prefixes[i] *= nums[i - 1] * prefixes[i - 1]
            answer[i] *= prefixes[i]

        # same for suffixes
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] *= nums[i + 1] * suffixes[i + 1]
            answer[i] *= suffixes[i]

        return answer
