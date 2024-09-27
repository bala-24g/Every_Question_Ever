class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(len(prices)+2)]

        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy ==0:
                    profit=max(dp[i+1][0],dp[i+1][1]-prices[i])
                else:
                    profit=max(dp[i+1][1],dp[i+2][0]+prices[i])
                dp[i][buy]=profit
        return dp[0][0]


#VEry similar to the others, but here it's of size n+2 and update logic is also a bit different.