
from typing import List
import heapq
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        MOD=100000 
        steps=[float('inf')]*MOD
        
        dq=[]
        
        heapq.heappush(dq,(0,start)) #steps,number
        
        while dq:
            step,number=heapq.heappop(dq)
            if number==end:
                return step
            for i in arr:
                new=(number*i)%MOD
                if steps[new]>step+1:
                    steps[new]=step+1
                    heapq.heappush(dq,(step+1,new))
        return -1
#Dijikstra