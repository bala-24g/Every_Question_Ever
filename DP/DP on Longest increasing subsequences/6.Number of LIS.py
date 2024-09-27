#Very similar to prev ones, but you've to maintain a count array to check the number of longest LIS till there, and also 
#The updating of the count array see condition.
#The criteria for getting ans is like you've to check dp array and then see if the longest subseq at that point is same as the maxlen, if yes then add the count of the longest subseq at that point to the ans from the count array.
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=max(dp[i],dp[j]+1)
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
        maxlen=max(dp)

        return sum(count[i] for i in range(len(nums)) if dp[i]==maxlen)


                
       

