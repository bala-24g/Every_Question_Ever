class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=[]
        directions={(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)}
        distance=[[float('inf')]*len(grid) for _ in range(len(grid))]

        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        
        heapq.heappush(queue,[0,[0,0]])
        distance[0][0]=1

        while queue:
            dist,[x,y]=queue.pop(0)

            if x==len(grid)-1 and y==len(grid)-1:
                return distance[x][y]

            for dx,dy in directions:
                newx=x+dx
                newy=y+dy

                if newx<len(grid) and newx>=0 and newy<len(grid) and newy>=0 and grid[newx][newy]==0 and distance[x][y]+1<distance[newx][newy]:
                    distance[newx][newy]=distance[x][y]+1
                    heapq.heappush(queue,[distance[newx][newy],[newx,newy]])
        if distance[-1][-1]==float('inf'):
            return -1
        
        return distance[len(grid)-1][len(grid)-1]
                    


        

#Dijikstra, but return the ans if found immediately.