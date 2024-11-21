class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # time: O(len(t))
        # space: O(1)
 
        if len(t) < len(s):
            return False
        if s == t or not len(s):
            return True

        s_ptr: int = 0
        for t_ptr in range(len(t)):
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            
            # Return true only if we've reached the ultimate end of s
            if s_ptr == len(s):
                return True

        return False
