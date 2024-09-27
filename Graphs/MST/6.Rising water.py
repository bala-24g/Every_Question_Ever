class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        distances=[[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        dq=[]
        distances[0][0]=0
        heapq.heappush(dq,[grid[0][0],0,0]) #x,y,maximum till then 
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]

        while dq:
            maxi,x,y=heapq.heappop(dq)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return maxi
            for dx,dy in dirs:
                if x+dx>=0 and x+dx<len(grid) and y+dy>=0 and y+dy<len(grid[0]):
                    newmaxi=max(maxi,grid[x+dx][y+dy])
                    if newmaxi<distances[x+dx][y+dy]:
                        distances[x+dx][y+dy]=newmaxi
                        heapq.heappush(dq,[newmaxi,x+dx,y+dy])
        return -1
            
        
#Dijikstra, but with the update condition changed as: if the distance of grid location is greater than the 
#Maximum value in the path upto that location(including the grid location)
#Then update the distance to that grid location and push it into dq.