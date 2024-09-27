class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        # Code here
        dp=[]
        for i in range(len(arr)):
            dp.append([1,[arr[i]]])
            
        maxlen=1
        ans=[arr[0]]
        
        for i in range(1,len(dp)):
            for j in range(i):
                if arr[i]>arr[j]:
                    if dp[i][0]<dp[j][0]+1:
                        dp[i][0]=dp[j][0]+1
                        dp[i][1]=dp[j][1][:]
                        dp[i][1].append(arr[i])
                        if len(dp[i][1])>maxlen:
                            maxlen=len(dp[i][1])
                            ans=dp[i][1]
        return ans
#Almost same as previous, but just keeping list also in the dp array instead of just the count. Also,making a copy of the list not the list itself from the previous elements.