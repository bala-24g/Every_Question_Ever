class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dq=deque()
        rows=len(mat)
        cols=len(mat[0])

        distance=[[float('inf')]*cols for _ in range(rows)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    dq.append([i,j,0])
                    distance[i][j]=0
        
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]

        while dq:
            x,y,dist=dq.popleft()

            for dx,dy in dirs:
                if x+dx>=0 and x+dx<len(mat) and y+dy>=0 and y+dy<len(mat[0]) and dist+1<distance[x+dx][y+dy]:
                    dq.append([x+dx,y+dy,dist+1])
                    distance[x+dx][y+dy]=dist+1
        return distance



    #Very basic bfs without visited, with condition to add element to dq being determined by the 
    #distance condition.