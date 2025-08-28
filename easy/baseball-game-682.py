from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # time: O(n)
        # space: O(n)
        scores = []

        for op in operations:
            if op == '+': # sums previous two scores
                first_score = scores[-2]
                second_score = scores[-1]
                scores.append(first_score + second_score)
            elif op == 'C': # invalidates previous score
                scores.pop()
            elif op == 'D': # doubles previous score
                recent_score = scores[-1]
                scores.append(recent_score * 2)
            else: # normal score appending
                scores.append(int(op))

        return sum(scores)
