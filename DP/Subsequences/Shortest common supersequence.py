#It's like very much like printing the LCS, this is a simpler logic for that too(make minor changes, in the second part while updating the s string, only uupdate when s1[i-1]==s2[j-1] and the rest just decrement. And don't do the while i>0 and j>0 for the second time.)
#Just look at the string s building logic after the LCS dp array construction.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        s=""

        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1

                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        i=len(str1)
        j=len(str2)

        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                s+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                s+=str1[i-1]
                i-=1
                
            else:
                s+=str2[j-1]
                j-=1
        while i>0:
            s+=str1[i-1]
            i-=1
        while j>0:
            s+=str2[j-1]
            j-=1
        return s[::-1]


        