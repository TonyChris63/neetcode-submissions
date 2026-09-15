class MinStack:

    def __init__(self):
        self.listt = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.listt.append(val)
        if self.minstack:
            less = min(self.minstack[-1], val)
            self.minstack.append(less)
        else:
            self.minstack.append(val)
    def pop(self) -> None:
        self.listt.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.listt[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
