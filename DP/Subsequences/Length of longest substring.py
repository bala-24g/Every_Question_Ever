#pretty similar to longest common subsequence but update condition is bit different
class Solution:
    def longestCommonSubstr(self, str1, str2):
        dp=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        res=0
        
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res=max(dp[i][j],res)
        return res 
                    