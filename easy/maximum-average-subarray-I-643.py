from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # space: O(1)
        # time: O(n)

        current_sum = sum(nums[0:k])
        max_avg = current_sum/k

        # Just track the current sum through appending next and removing most left each loop
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            current_avg = current_sum / k
            if current_avg > max_avg:
                max_avg = current_avg
        return max_avg
