from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # space: O(s + t)
        # time: O(s + t)
        s_letters = Counter(s)
        t_letters = Counter(t)
        return s_letters == t_letters
