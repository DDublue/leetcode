class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # time: O(n+m)
        # space: O(n+m)
        
        i = 0
        word1Length = len(word1)
        word2Length = len(word2)
        lettersOfMergedWord = []

        # First loop through as far as possible for both
        while i < word1Length and i < word2Length:
            lettersOfMergedWord.append(word1[i])
            lettersOfMergedWord.append(word2[i])
            i += 1

        # Then loop whichever word is longer to get the rest
        for j in range(i, word1Length):
            lettersOfMergedWord.append(word1[j])
        for j in range(i, word2Length):
            lettersOfMergedWord.append(word2[j])

        return "".join(lettersOfMergedWord)
