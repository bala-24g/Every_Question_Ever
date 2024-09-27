class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[0]*2 for _ in range(len(prices)+1)]

        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy==0:
                    profit=max(dp[ind+1][0],-prices[ind]+dp[ind+1][1])
                else:
                    profit=max(dp[ind+1][1],prices[ind]+dp[ind+1][0]-fee)
                
                dp[ind][buy]=profit
        return (dp[0][0])


#Very similar logic to the previous ones, except add a fee to the buying part alone.