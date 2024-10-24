class Solution:
    def findMatching(self, text, pattern):
        # Code here
        m=len(pattern)
        n=len(text)
        
        for i in range(n-m+1):
            if text[i:i+m]==pattern:
                return i
        return -1
    #Very basic 