class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        timings=[float('inf')]*(n+1)
        timings[0]=0

        graph=defaultdict(list)

        for u,v,w in times:
            graph[u].append([v,w])
        
        dq=[]

        heapq.heappush(dq,[0,k])
        timings[k]=0

        while dq:
            time,node=heapq.heappop(dq)
            for nei,dt in graph[node]:
                if timings[node]+dt<timings[nei]:
                    timings[nei]=timings[node]+dt
                    heapq.heappush(dq,[timings[nei],nei])
        maxi=0
        for i in timings:
            maxi=max(maxi,i)
        if maxi==float('inf'):
            return -1
        return maxi
        
        #dijikstra