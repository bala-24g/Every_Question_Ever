#Very similar to oranges, but the problem statement is a bit different so the bfs dq.append logic is diff;
# Also tc of x and y boundaries correctly.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dq=deque()
        
        original=image[sr][sc]
        if original==color:
            return image
        image[sr][sc]=color
        dq.append([sr,sc])
    

        dirs=[[-1,0],[0,-1],[0,1],[1,0]]
        while dq:
            x, y = dq.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # Check if the adjacent cell is within bounds and has the original color
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == original:
                    dq.append([nx, ny])  # Add the new cell to the queue for BFS
                    image[nx][ny] = color  # Change the color of the new cell
        
        return image