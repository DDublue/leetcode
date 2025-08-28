from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # space: O(1)
        # time: O(n log m)

        def ceiling(dividend, divisor):
            return -(-dividend // divisor)

        # Use binary to find minimum eating rate
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += ceiling(pile, mid)
            
            # Unused hours, so must eat slower
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        
        return low
