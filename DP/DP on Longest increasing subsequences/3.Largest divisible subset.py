class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp=[]
        nums.sort()
        maxlen=1
        ans=[nums[0]]
        

        for i in range(len(nums)):
            dp.append([1,[nums[i]]])
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i][0]<dp[j][0]+1:
                    dp[i][0]=1+dp[j][0]
                    dp[i][1]=dp[j][1][:]
                    dp[i][1].append(nums[i])
                    if len(dp[i][1])>maxlen:
                        maxlen=len(dp[i][1])
                        ans=dp[i][1]
        return ans 
#This is very similar to 2, except here you have to sort and the initial comparison is different.