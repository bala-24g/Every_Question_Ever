class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        grid=obstacleGrid

        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0

        dp=[[0]*cols for _ in range(rows)]
        dp[0][0]=1

        for i in range(1,rows):
            if grid[i][0]==0:
                dp[i][0]=dp[i-1][0]
            else:
                dp[i][0]=0
        for j in range(1,cols):
            if grid[0][j]==0:
                dp[0][j]=dp[0][j-1]
            else:
                dp[0][j]=0



        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:  # Obstacle blocks this cell
                    dp[i][j] = 0

        return dp[-1][-1]



    #Similar to before, but grid initialisation for the first row and column is different and the updation is done only if the grid entry is not an obstacle.