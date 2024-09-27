class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]

        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for limit in range(1,k+1):
                    profit=0
                    if buy==0:
                        profit=max(dp[ind+1][0][limit],-prices[ind]+dp[ind+1][1][limit])
                    else:
                        profit=max(dp[ind+1][1][limit],prices[ind]+dp[ind][0][limit-1])
                    dp[ind][buy][limit]=profit
        return dp[0][0][k]

#same as before, but here we have k instead of 2 as limit.