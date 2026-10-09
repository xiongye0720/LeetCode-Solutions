class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr = len(prices) - 2
        # Track the highest selling price to the right.
        maxPrice = prices[-1]
        diff = 0

        while ptr >= 0:
            if prices[ptr] > maxPrice:
                maxPrice = prices[ptr]
            else:
                # Check the profit from buying on this day.
                if maxPrice - prices[ptr] > diff:
                    diff = maxPrice - prices[ptr]
            ptr = ptr - 1

        return diff