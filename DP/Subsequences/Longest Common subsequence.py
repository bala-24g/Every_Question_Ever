# Logic: DP array logic: 2D array where each position returns the longest subsequences with substrings upto that position.
#DP updating logic: Check if the new elements in both the strings are same , if it is then just change the count by count by 1 from the prev one, else check keep the count as max(one letter less from 1st string or 1 letter less from second string)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

        