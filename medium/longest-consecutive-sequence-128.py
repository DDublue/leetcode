from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # space: O(n)
        # time: O(n)

        max_length = 0
        nums_hash = dict()

        # add nums to hash for O(1) lookups
        for num in nums:
            nums_hash[num] = 1

        # if num-1 exists, num is not the starting of its sequence.
        # else it is, so now we count its length and track the max length
        for num in nums_hash:
            current_length = 1
            if num - 1 not in nums_hash:
                inner_num = num + 1
                while inner_num in nums_hash:
                    current_length += 1
                    inner_num += 1
            max_length = max(max_length, current_length)

        return max_length
