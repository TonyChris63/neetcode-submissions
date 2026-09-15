class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        c = 0
        while n > 1:
            c = a + b
            a = b
            b = c
            n -= 1

        return b


