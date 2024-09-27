class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def helper(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            r=0
            l=0
            while r<len(s1):
                if l<len(s2) and s1[r]==s2[l] :
                    r+=1
                    l+=1
                else:
                    r+=1
            return (r==len(s1) and l==len(s2))

        words.sort(key=len)
        dp=[1]*len(words)

        for i in range(1,len(words)):
            for j in range(i):
                if helper(words[i],words[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        
#Very similar logic, except have to check if the jth element is a predecessor of ith element where the helper function comes in.