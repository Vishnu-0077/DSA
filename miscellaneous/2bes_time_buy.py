class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        mini = prices[0]
        ans = 0
        for i in range(1,n):
            ans = max(ans,prices[i]-mini)
            mini = min(mini,prices[i])
        return ans
            

        