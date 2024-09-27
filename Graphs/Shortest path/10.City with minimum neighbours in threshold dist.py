class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=defaultdict(list)

        for u,v,w in edges:
            graph[u].append([v,w]) #parent->node,weight
            graph[v].append([u,w])
        
        

        distances=[[float('inf')]*n for _ in range(n)] #from, to

        for i in range(n):
            for j in range(n):
                if i==j:
                    distances[i][j]=0
        
        for i in graph.keys():
            for j in graph[i]:
                distances[i][j[0]]=j[1]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j]=min(distances[i][j],distances[i][k]+distances[k][j])
        
        count=[0]*n

        for i in range(n):
            for j in range(n):
                if distances[i][j]<=distanceThreshold:
                    count[i]+=1
        
        mincount=float('inf')
        ans=0

        for i in range(n):
            if mincount>=count[i]:
                mincount=count[i]
                ans=i
        return ans


#Floyd Walsh algorithm.
#This uses like an intermediate variable (k) to get the distance from city i to j via k, if the distance through k is lesser than the current minimum distance, then update the distance at that square in the grid.