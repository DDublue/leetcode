from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # space: O(1)
        # time: O(log mn)
        
        start = 0
        end = len(matrix) - 1
        row = -1

        left = 0
        right = len(matrix[0]) - 1

        # Binary search for the row that contains the target
        while start <= end:
            mid = start + (end - start) // 2
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                row = mid
                break
        
        # No row contains the target
        if row == -1:
            return False

        # Binary search for the target in the row
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        
        return False
