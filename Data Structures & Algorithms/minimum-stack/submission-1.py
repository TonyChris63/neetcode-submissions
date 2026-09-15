class MinStack:

    def __init__(self):
        self.listt = []
        self.mins = []
    def push(self, val: int) -> None:
        self.listt.append(val)
        val = min(val, 
        self.mins[-1] if self.mins
        else val)
        self.mins.append(val)
    def pop(self) -> None:
        self.listt.pop()
        self.mins.pop()
    def top(self) -> int:
        return self.listt[-1]
    def getMin(self) -> int:
        return self.mins[-1]
