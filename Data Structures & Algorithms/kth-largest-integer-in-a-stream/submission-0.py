class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.stream = nums
        self.c = k
    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[-self.c]
