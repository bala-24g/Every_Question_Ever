class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=prices[0]
        res=0
        for i in range(len(prices)):
            if prices[i]<=minsofar:
                minsofar=prices[i]
            res=max(res,prices[i]-minsofar)
        return res
#Keep a track of current minimum (which will be the cost price) and subtract the corresponding array elements (selling price) from minimum.