from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # space: O(n)
        # time: O(n)
        
        counter = Counter(text)
        for letter in {'b', 'a', 'l', 'o', 'n'}:
            if letter not in counter:
                return 0

        # 2 l's and o's for every b, a, n
        counter['l'] //= 2
        counter['o'] //= 2
        balloon_letter_count = [
            counter['b'],
            counter['a'],
            counter['l'],
            counter['o'],
            counter['n']
        ]

        return min(balloon_letter_count)
