class Solution:
    def romanToInt(self, s: str) -> int:
        # time: O(len(s))
        # space: O(1)

        romanToIntMap: dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return romanToIntMap[s]

        integer: int = 0
        i: int = len(s) - 1
        while i > 0:
            prevChar = s[i-1]
            currChar = s[i]

            # Add the roman value then substract if needed
            integer += romanToIntMap[currChar]
            if prevChar == "I" and (currChar == "V" or currChar == "X"):
                integer -= romanToIntMap[prevChar]
                i -= 1
            elif prevChar == "X" and (currChar == "L" or currChar == "C"):
                integer -= romanToIntMap[prevChar]
                i -= 1
            elif prevChar == "C" and (currChar == "D" or currChar == "M"):
                integer -= romanToIntMap[prevChar]
                i -= 1
            i -= 1

        # Prevents final conversion with first and last roman letters (if occurs)
        if i == 0:
            integer += romanToIntMap[s[0]]

        return integer
