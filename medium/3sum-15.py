from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(n^2)
        # space: O(n^2)

        # This makes it more optimal for comparison
        nums.sort()
        
        triplets = set()
        for i, target in enumerate(nums):
            left = 0
            right = len(nums) - 1

            # Sets current number as the target.
            # Use two pointers to iterate and find two numbers that sum to the negative of the target.
            # Behaves like two sum.
            while left < i and right > i and left < right:
                if nums[left] + nums[right] == -target:
                    triplet = tuple(sorted([target, nums[left], nums[right]]))
                    triplets.add(triplet)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -target:
                    right -= 1
                else:
                    left += 1

        return [list(triplet) for triplet in triplets]
