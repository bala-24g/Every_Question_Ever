class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dq=[]
        distances=[[float('inf')]* len(heights[0]) for _ in range(len(heights))]

        dirs=[[-1,0],[0,-1],[1,0],[0,1]]

        heapq.heappush(dq,[0,[0,0]])
        
        rows=len(heights)
        cols=len(heights[0])

        while dq:
            dist,[x,y]=heapq.heappop(dq)
            
            for dx,dy in dirs:
                newx=x+dx
                newy=y+dy

                if newx>=0 and newx<rows and newy>=0 and newy<cols:
                    newdist=max(dist,abs(heights[newx][newy]-heights[x][y]))
                    if newdist<distances[newx][newy]:
                        distances[newx][newy]=newdist
                        heapq.heappush(dq,[newdist,[newx,newy]])
                    
        if distances[-1][-1]==float('inf'):
            return 0
        return distances[-1][-1] 
#Dijikstra, but push logic is bit different.