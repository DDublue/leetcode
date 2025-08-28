class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # space: O(1)
        # time: O(log n)

        if num == 1:
            return True

        left = 2
        right = num

        # Uses opposite of squaring as the condition
        while left < right:
            mid = left + (right - left) // 2
            if num / mid == mid:
                return True
            elif num / mid < mid:
                right = mid
            else:
                left = mid + 1

        return False
