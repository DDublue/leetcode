from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # space: O(1)
        # time: O(1)

        # setup hashmap
        hashmap = {}
        for i in range(9):
            hashmap[f"r{i}"] = set()
            hashmap[f"c{i}"] = set()
        for i in range(3):
            for j in range(3):
                hashmap[f"box{i}{j}"] = set()
        
        # check board
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                row_set = hashmap[f"r{i}"]
                col_set = hashmap[f"c{j}"]
                box_set = hashmap[f"box{(i // 3) % 3}{(j // 3) % 3}"]
                if cell == ".":
                    continue

                if cell in row_set:
                    return False
                else:
                    row_set.add(cell)
                    
                if cell in col_set:
                    return False
                else:
                    col_set.add(cell)

                if cell in box_set:
                    return False
                else:
                    box_set.add(cell)
        
        return True
