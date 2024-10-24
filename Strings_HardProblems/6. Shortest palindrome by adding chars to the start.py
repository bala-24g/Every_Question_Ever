class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r=s[::-1]
        for i in range(len(r)+1):
            if s.startswith(r[i:]):
                return r[:i]+s
    #What happens is that you compare how much of the reversed string matches, then reverse that part and add it to s; so that it becomes a palindrome.
        