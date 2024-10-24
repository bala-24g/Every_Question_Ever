class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(number):
            number=str(number)
            lst=list(number)
            cnt=1
            ans=""
            for i in range(1,len(lst)):
                if lst[i]==lst[i-1]:
                    cnt+=1
                else:
                    ans+=str(cnt)+lst[i-1]
                    cnt=1
            ans += str(cnt) + lst[-1]
            return ans 
        t=1
            
        for i in range(n-1):
            t=helper(t)
        return str(t)
            

#Keep track of number of numbers