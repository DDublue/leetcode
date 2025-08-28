class MinStack:

    def __init__(self):
        self.stack = [] # List[List[a,b]] where a = val, b = min

    def push(self, val: int) -> None:
        min_num = val
        if self.stack:
            min_num = min(val, self.stack[-1][1])
        self.stack.append([val, min_num])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        min_num = 2**31 - 1
        if self.stack:
            min_num = self.stack[-1][1]
        return min_num

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
