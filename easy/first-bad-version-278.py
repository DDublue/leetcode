# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # space: O(1)
        # time: O(log n)
        
        left = 1
        right = n

        # Binary search until first bad is found
        while left < right:
            mid = left + (right - left) // 2
            
            isBad = isBadVersion(mid)
            if isBad:
                right = mid - 1
            else:
                left = mid + 1
        
        return left if isBadVersion(left) else left + 1
