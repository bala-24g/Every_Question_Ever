class Solution:
    def longestPrefix(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            if s[:i]==s[-i:]:
                if i>len(ans):
                    ans=s[:i]
        return ans 
#Compare the first to last and last to first components and see if they're same. 
        