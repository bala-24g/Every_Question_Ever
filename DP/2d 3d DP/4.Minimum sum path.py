class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        dp=[[float('inf')]*cols for _ in range(rows)]

        dp[0][0]=grid[0][0]

        for i in range(1,rows):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,cols):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j]=min(dp[i][j],dp[i][j-1]+grid[i][j])
                dp[i][j]=min(dp[i][j],dp[i-1][j]+grid[i][j])
        return dp[-1][-1]
#Standard: rows, cols as base cases; then update condition.