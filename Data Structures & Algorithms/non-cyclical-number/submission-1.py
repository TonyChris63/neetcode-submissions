class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        c = 0
        def sumOfDigsSQ(b):
            if b < 10:
                return b * b
            else:
                return ((b % 10) ** 2) + sumOfDigsSQ(b // 10)
        c = sumOfDigsSQ(n)
        while c not in seen:
            if c == 1:
                return True
            else:
                seen.add(c)
                c = sumOfDigsSQ(c)
        return False
