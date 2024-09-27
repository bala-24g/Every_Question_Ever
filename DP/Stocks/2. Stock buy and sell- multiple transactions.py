class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1]*2 for _ in range(len(prices)+1)]

        dp[len(prices)][0]=0
        dp[len(prices)][1]=0

        for ind in range(len(prices)-1,-1,-1):
            for sell in range(2):
                profit=0
                if sell==0:
                    profit=max(dp[ind+1][0],-prices[ind]+dp[ind+1][1])
                else:
                    profit=max(dp[ind+1][1],prices[ind]+dp[ind+1][0])
                dp[ind][sell]=profit
        return dp[0][0]

#Create a dp array from 0 to len of prices+1. Columns are 2: buy and sell. Initialise the last 
# elements (buy and sell) with 0. Then traverse back, and for each sell==0 and 1; if sell==1: then subtract
#The prev current element from the prev profit and compare it with the profit at the prev (already traversed)
#element. Then for sell = 1; add the current element from the prices array and check if it is greater than the profit at the previous element.
