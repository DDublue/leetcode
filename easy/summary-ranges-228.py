from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # time: O(n)
        # space: O(n)

        if not nums:
            return []
        
        summaryRangeList = []
        # track start and end of ranges
        anchorNum = prevNum = nums[0]
        for i, num in enumerate(nums[1:]):
            if num - prevNum > 1:
                if anchorNum == prevNum:
                    summaryRangeList.append(f"{prevNum}")
                else:
                    summaryRangeList.append(f"{anchorNum}->{prevNum}")
                anchorNum = num
            prevNum = num
            
        # do final num    
        if anchorNum == prevNum:
            summaryRangeList.append(f"{prevNum}")
        else:
            summaryRangeList.append(f"{anchorNum}->{prevNum}")
            
        return summaryRangeList
