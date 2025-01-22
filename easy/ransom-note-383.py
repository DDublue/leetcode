class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # space: O(n)
        # time: O(n)

        # setup counter
        letters_owned = dict()
        for letter in magazine:
            if letter in letters_owned:
                letters_owned[letter] += 1
            else:
                letters_owned[letter] = 1
        
        # check valid ransomNote
        for letter in ransomNote:
            if letter not in letters_owned or letters_owned[letter] < 1:
                return False
            letters_owned[letter] -= 1
        
        return True
            