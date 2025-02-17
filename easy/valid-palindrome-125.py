class Solution:
    def isPalindrome(self, s: str) -> bool:
        # space: O(1)
        # time: O(n)

        left = 0
        right = len(s) - 1

        while left < right:
            # Alphanumerics don't count
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > -1 and not s[right].isalnum():
                right -= 1
            
            if not (left < right): # left passed right, so break
                break

            if s[left].lower() != s[right].lower(): # not the same, so not a palindrome
                return False

            left += 1
            right -= 1

        return True
