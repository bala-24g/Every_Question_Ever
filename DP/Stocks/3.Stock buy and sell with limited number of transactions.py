class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # Create a 3D DP table with dimensions (n+1) x 2 x 3 and initialize it to 0 values
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    # If buy == 0, we can buy; if buy == 1, we can sell
                    if buy == 0:
                        # Max profit between not buying or buying and transitioning to selling state
                        dp[ind][buy][cap] = max(dp[ind + 1][0][cap], -prices[ind] + dp[ind + 1][1][cap])
                    else:
                        # Max profit between not selling or selling and transitioning to buying state with one less transaction
                        dp[ind][buy][cap] = max(dp[ind + 1][1][cap], prices[ind] + dp[ind + 1][0][cap - 1])
        
        # Return the maximum profit starting at day 0, with 0 stock and 2 transactions allowed
        return dp[0][0][2]

#Same logic as 2, but an added inner column for number of transactions.
#Cap starts from 1,3 and not for i in range(3); because i-1 when buying can be done easily.