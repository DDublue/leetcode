from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # space: O(mn)
        # time: O(mn)

        m = len(matrix)
        n = len(matrix[0])
        spiral_order = []
        dr, dc = 1, 0
        first_row, first_col = 0, 0
        last_row, last_col = m - 1, n - 1

        # brute force rotations and traversals
        while first_row <= last_row or first_col <= last_col:
            if dr > 0: # right
                for i in range(first_col, last_col + 1):
                    if first_row < m and i < n and matrix[first_row][i] != 1000:
                        spiral_order.append(matrix[first_row][i])
                        matrix[first_row][i] = 1000
                first_row += 1
            elif dr < 0: # left
                for i in range(last_col, first_col - 1, -1):
                    if last_row > -1 and i < n and matrix[last_row][i] != 1000:
                        spiral_order.append(matrix[last_row][i])
                        matrix[last_row][i] = 1000
                last_row -= 1
            elif dc > 0: # up
                for i in range(last_row, first_row - 1, -1):
                    if i < m and first_col < n and matrix[i][first_col] != 1000:
                        spiral_order.append(matrix[i][first_col])
                        matrix[i][first_col] = 1000
                first_col += 1
            elif dc < 0: # down
                for i in range(first_row, last_row + 1):
                    if i < m and last_col > -1 and matrix[i][last_col] != 1000:
                        spiral_order.append(matrix[i][last_col])
                        matrix[i][last_col] = 1000
                last_col -= 1
            dr, dc = dc, -dr # rotation

        return spiral_order
