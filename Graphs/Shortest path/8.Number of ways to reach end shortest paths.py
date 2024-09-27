class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=(10**9)+7
        time=[float('inf')]*n
        ways=[0]*n

        dq=[]
        graph=defaultdict(list)

        for u,v,w in roads:
            graph[u].append([v,w])
            graph[v].append([u,w])
        
        heapq.heappush(dq,[0,0])#time,node
        ways[0]=1

        while dq:
            t,node=heapq.heappop(dq)

            for nei,dt in graph[node]:
                if time[nei]>t+dt:
                    time[nei]=t+dt
                    ways[nei]=ways[node]
                    heapq.heappush(dq,[t+dt,nei])
                elif time[nei]==t+dt:
                    ways[nei]= (ways[nei] + ways[node]) % MOD
        return ways[-1]%(MOD)
#See heapq push logics. Otherwise dijkstra