class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxsell = 0

        for sell in prices:
            maxsell = max(maxsell, sell - minbuy)
            minbuy = min(minbuy, sell)

        return maxsell
        