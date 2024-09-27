class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows=len(board)
        cols=len(board[0])

        dq=deque()
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    if i==0 or i==rows-1 or j==0 or j==cols-1:
                        dq.append([i,j])
                        board[i][j]="T"

        while dq:
            x,y=dq.popleft()
            
            for dx,dy in dirs:
                if x+dx>=0 and x+dx<rows and y+dy>=0 and y+dy<cols and board[x+dx][y+dy]=="O":
                    board[x+dx][y+dy]="T"
                    dq.append([x+dx,y+dy])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
    

                
#BFS, with starting at the point where we want to single out. I.E; in BFS usually start with places where you
#Want to eliminate/identify and move from there.
#Here we have to find out all Os connected to corner Os, and single them out.
#So, we make a queue with the corner Os, and mark using BFS all Os attached to them with a temporary marker T.
#Then we change the Ts to Os and keep the rest as Xs as they are surrounded by Xs or X convertibles on all sides.
