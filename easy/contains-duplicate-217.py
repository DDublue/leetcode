from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # space: O(n)
        # time: O(n)
        
        existing_nums_set = set()
        for num in nums:
            if num not in existing_nums_set:
                existing_nums_set.add(num)
            else:
                return True
        return False
