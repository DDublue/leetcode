from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # time: O(n)
        # space: O(n)

        stack = []

        for token in tokens:
            if token == '+':
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand + second_operand)
            elif token == '-':
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand - second_operand)
            elif token == '*':
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand * second_operand)
            elif token == '/':
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(int(first_operand / second_operand))
            else:
                stack.append(int(token))

        return stack[0]
