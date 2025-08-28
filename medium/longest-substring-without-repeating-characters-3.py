class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # space: O(n)
        # time: O(n)
        
        start = 0
        max_len = 0
        seen = {}

        for i in range(len(s)):
            char = s[i]
            if char in seen and seen[char] >= start: # found dupe
                start = seen[char] + 1
            else: # no dupe, continue
                max_len = max(max_len, i - start + 1)
            seen[char] = i

        return max_len
