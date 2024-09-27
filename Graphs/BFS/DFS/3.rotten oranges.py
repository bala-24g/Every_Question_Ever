#Rotten oranges, very standard bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis=[[False]*len(grid[0])for _ in range(len(grid))]
        dq=deque()
        fresh=0
        rotten=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    dq.append([i,j,0])
                    vis[i][j]=True
                    rotten+=1
                elif grid[i][j]==1:
                    fresh+=1
        count=rotten
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]
        t=0
        while dq:
            x,y,t=dq.popleft()
            for dx,dy in dirs:
                if x+dx<len(grid) and x+dx>=0 and y+dy<len(grid[0]) and y+dy>=0 and vis[x+dx][y+dy]==False and grid[x+dx][y+dy]==1:
                    vis[x+dx][y+dy]=True
                    count+=1
                    dq.append([x+dx,y+dy,t+1])
        if count==rotten+fresh:
            return t
        else:
            return -1

            


        