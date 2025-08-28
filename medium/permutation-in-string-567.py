class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # space: O(n)
        # time: O(n)

        left = 0
        s1_freq = {}
        s2_freq = {}

        # Used for comparison
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        # The checking
        for right, char in enumerate(s2):
            if char not in s1_freq:
                s2_freq = {}
                left = right + 1
            else: # still a valid, potential permutation
                s2_freq[char] = s2_freq.get(char, 0) + 1
                if s2_freq[char] > s1_freq[char]:
                    s2_freq[char] -= 1
                    left += 1
                    
                if s1_freq.items() == s2_freq.items(): # second check for true permutation
                    temp_freq = {}
                    for letter in s2[left:right+1]:
                        temp_freq[letter] = temp_freq.get(letter, 0) + 1
                    if s1_freq.items() == temp_freq.items():
                        # print(f"s1: {s1_freq}; s2: {s2_freq}")
                        return True
        
        return False

                