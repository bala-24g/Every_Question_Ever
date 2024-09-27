from typing import List
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        distance=[float('inf')]*V
        queue=[]
        distance[S]=0
        heapq.heappush(queue,[distance[S],S])
        while queue:
            curdist,node=heapq.heappop(queue)
            for nei,dist in adj[node]:
                if curdist+dist<distance[nei]:
                    distance[nei]=curdist+dist
                    heapq.heappush(queue,[distance[nei],nei])
        for i in range(len(distance)):
            if distance[i]==float('inf'):
                distance[i]=-1
        return distance
#Data structures: heapq,distance array and given adj list.
#Keep updating and pushing distance,vertex pairs into heapq.