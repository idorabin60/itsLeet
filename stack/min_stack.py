class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # This will track the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push onto min_stack if it's empty or the new value is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            value = self.stack.pop()
            # If popped value is the current minimum, remove it from min_stack as well
            if value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None  # or raise an error if preferred

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # or raise an error if preferred


# Example usage:
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())  # prints 0
minStack.pop()
print(minStack.top())     # prints 2
print(minStack.getMin())  # prints 1
