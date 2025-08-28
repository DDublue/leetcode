class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # space: O(1)
        # time: O(n)
        # Had some help thinking about the logic

        left = 0
        max_count = 0
        count = {}

        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_count = max(max_count, count[char])

            if ((right - left + 1) - max_count) > k:
                count[s[left]] -= 1
                left += 1
            
        return len(s) - left
