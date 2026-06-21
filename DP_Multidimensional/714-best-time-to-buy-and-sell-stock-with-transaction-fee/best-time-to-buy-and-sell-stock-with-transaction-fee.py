class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)

        hold = [0] * n
        cash = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            # keep holding OR buy today
            hold[i] = max(
                hold[i-1],
                cash[i-1] - prices[i]
            )

            # keep cash OR sell today
            cash[i] = max(
                cash[i-1],
                hold[i-1] + prices[i] - fee
            )

        return cash[-1]