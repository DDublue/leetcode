from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)

        closestNumber = nums[0]
        for num in nums:
            if abs(num) < abs(closestNumber): # current num distance is smaller
                closestNumber = num
            elif num + closestNumber == 0 and num > closestNumber: # same distances but current num is a positive value
                closestNumber = num
        return closestNumber
