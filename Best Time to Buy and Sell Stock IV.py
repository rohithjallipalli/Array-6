""""// Time Complexity : O(n*k)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        if k >= len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float('inf')] * (k + 1)
        buy[0] = prices[0]
        sell = [0] * (k + 1)

        for i in range(len(prices)):
            for j in range(1, k + 1):
                buy[j] = min(buy[j], prices[i] - sell[j - 1])
                sell[j] = max(sell[j], prices[i] - buy[j])
        return sell[k]
