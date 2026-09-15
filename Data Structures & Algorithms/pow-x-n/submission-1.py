class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(b, m):
            if m == 0:
                return 1
            if m == 1:
                return b
            if m % 2 == 0:
                return power(b * b, m//2)
            if m % 2 != 0:
                return b * power(b * b, m//2)
        if n >= 0:
            return power(x,n)
        if n < 0:
            return 1/power(x,abs(n))