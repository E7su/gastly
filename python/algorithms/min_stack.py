class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = math.inf
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        if x <= self.getMin():
            self.min_stack.append(x)
            self.minimum = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] is self.minimum:
            min_stack_size = len(self.min_stack)
            self.min_stack.pop()
            if min_stack_size is not 1:
                self.minimum = self.min_stack[-1]
            else:
                self.minimum = sys.maxsize

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
