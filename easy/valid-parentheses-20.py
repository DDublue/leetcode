class Solution:
    def isValid(self, s: str) -> bool:
        # space: O(1)
        # time: O(n)
        
        stack = []

        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            elif bracket == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif bracket == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif bracket == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(bracket)

        # Non-empty stack means still leftover brackets, which means invalid
        return len(stack) == 0
