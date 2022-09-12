""""// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxi = float('-inf')
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)
        return maxi

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l=0
#         r=1

#         maxprofit=0

#         while r<len(prices):
#             if prices[l]<prices[r]:
#                 x=prices[r]-prices[l]
#                 maxprofit=max(x, maxprofit)
#             else:
#                 l=r
#             r+=1
#         return maxprofit