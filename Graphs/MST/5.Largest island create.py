from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j, ref):
            grid[i][j] = ref
            dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            size = 1
            dq = deque()
            dq.append([i, j])

            while dq:
                x, y = dq.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = ref
                        size += 1
                        dq.append([nx, ny])

            return size

        ref = 2
        sizes = {}
        maxsize = 0

        # Step 1: Label all islands with BFS and store their sizes
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = bfs(i, j, ref)
                    sizes[ref] = size
                    maxsize = max(size, maxsize)
                    ref += 1

        # Step 2: Check every water cell (0) and calculate the possible island size if we flip it
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        maxi = maxsize  # Start with the largest island we already have

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    size = 1  # Start with size 1 because we flip this water cell
                    visited = set()
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] > 1:
                            if grid[ni][nj] not in visited:  # Avoid counting the same island twice
                                visited.add(grid[ni][nj])
                                size += sizes[grid[ni][nj]]
                    maxi = max(maxi, size)

        return maxi
#Create largest island by converting one water block into land. Used BFS,  no DSU.