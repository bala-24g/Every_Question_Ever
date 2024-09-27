#Minimum insertions to make a string a palindrome, almost same as longest common palindromic subsequence\
#But return length of string-length of longest common subseq btw string and its reverse
#A modified qn I am not including here is: minimum number of deletions in 2 strings to make them same, which is like
#finding longest common subsequence and subtracting that from each of the lengths of the 2 strings.

class Solution:
    def minInsertions(self, s: str) -> int:
        normal=s
        reverse=s[::-1]

        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]

        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if normal[i-1]==reverse[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return len(s)-dp[-1][-1]
        
        