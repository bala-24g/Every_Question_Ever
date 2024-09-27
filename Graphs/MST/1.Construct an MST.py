from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        heap=[]
        
        vis=[-1]*V
        
        heapq.heappush(heap,((0,0)))
        res=0
        
        while heap:
            weight,node=heapq.heappop(heap)
            
            if vis[node]==1:
                continue
            
            if vis[node]==-1:
                res+=weight
                vis[node]=1
                for nei in adj[node]:
                    v,wt=nei[0],nei[1]
                    if vis[v]==-1:
                        heapq.heappush(heap,(wt,v))
                        
                    
        
        return res 
    
#Minimum spanning tree: Have a visited array, and have a minheap. Push (distance,node) pairs into the minheap. Initialise minheap with (0,0) . Result=0. While minheap, Pop minheap and if the popped node is not visited, add the weight to result, mark the popped node as visited. Then check its adjoining nodes and if they haven’t been visited add (wt,nei) to the minheap. Return res. 