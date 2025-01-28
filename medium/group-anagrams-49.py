from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # space: O(n)
        # time: O(nlogn)
        
        anagrams_by_letters = defaultdict(list)
        for s in strs:
            anagram = "".join(sorted(s))
            anagrams_by_letters[anagram].append(s)
        
        return list(anagrams_by_letters.values())
