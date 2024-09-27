
from typing import List


class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        dp1=[1]*len(nums)
        dp2=[1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp1[i]=max(dp1[i],dp1[j]+1)
        
        for i in range(len(nums)-1,0,-1):
            for j in range(len(nums)-1,i-1,-1):
                if nums[i]>nums[j]:
                    dp2[i]=max(dp2[i],dp2[j]+1)
        maxi=0
        for i in range(len(nums)):
            if dp2[i]!=1 and dp1[i]!=1:
                
                maxi=max(maxi,dp1[i]+dp2[i]-1)
                
            
        return maxi
#Very similar to previous ones, here we are calculating reverse also what the increasing subseq is. Then we check if there
#is an increasing and decreasing subseq and it's not just default one in the last condition, and add the two dp arrays' elements and subtract -1 and check what you get.