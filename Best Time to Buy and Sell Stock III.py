""""// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = prices[0]
        sell1 = 0
        buy2 = prices[0] - sell1
        sell2 = prices[0] - buy2

        for i in range(1, len(prices)):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2


""""// Time Complexity : O(n^3)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         maxi = 0
#         for i in range(len(prices)):
#             max1 = 0
#             for j in range(i + 1, len(prices)):
#                 if prices[j] > prices[i]:
#                     max1 = prices[j] - prices[i]
#                 max2 = 0
#                 mini = float('inf')
#                 for k in range(j + 1, len(prices)):
#                     mini = min(mini, prices[k])
#                     max2 = max(max2, abs(prices[k] - mini))
#                 maxi = max((max1 + max2), maxi)
#         return maxi