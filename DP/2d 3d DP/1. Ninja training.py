class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        dp=[[0]*3 for i in range(len(arr))]
        
        dp[0][0]=arr[0][0]
        dp[0][1]=arr[0][1]
        dp[0][2]=arr[0][2]
        
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + arr[i][0]  # Task 0
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + arr[i][1]  # Task 1
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[i][2]  # Task 2
        maxi=-1
        for i in dp[-1]:
            maxi=max(maxi,i)
        return maxi
#Simple logic