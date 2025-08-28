from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(n)
        # space: O(n)
        
        n = len(temperatures)
        answer = [0] * n
        stack = []

        t = temperatures # just an alias
        # Iterate days; keep a stack of (index, temp) with strictly decreasing temps.
        # When current temp is higher, pop and record how many days were waited.
        for i in range(n):
            while stack and t[i] > stack[-1][-1]:
                index, _ = stack.pop()
                answer[index] = i - index

            stack.append((i, t[i]))

        return answer
