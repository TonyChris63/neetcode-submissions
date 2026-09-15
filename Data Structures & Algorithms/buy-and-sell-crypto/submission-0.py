class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        counter1 = 0
        counter2 = 0
        for b in prices:
            counter1 += 1
            for s in prices:
                counter2 += 1
                if counter1 >= counter2:
                    continue
                diff = s - b
                if diff > profit:
                    profit = diff
            counter2 = 0
        return profit
