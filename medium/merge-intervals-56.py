from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # space: O(n)
        # time: O(nlogn)

        sorted_intervals = sorted(intervals)
        non_overlaps = []

        anchor = sorted_intervals[0] # [a, b]
        for i, rangee in enumerate(sorted_intervals[1:]):
            if anchor[1] >= rangee[0]:
                if rangee[1] > anchor[1]: # only extend anchor if rangee bigger
                    anchor[1] = rangee[1]
            else: # non-overlapping interval reached
                non_overlaps.append(anchor)
                anchor = rangee
        non_overlaps.append(anchor) # for final merged interval

        return non_overlaps
