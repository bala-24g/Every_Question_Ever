from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = [0] * len(graph)  # 0 means uncolored, 1 and -1 will be the two colors

        # Go through each node in case the graph is disconnected
        for start in range(len(graph)):
            if vis[start] == 0:  # If the node is uncolored, perform BFS
                dq = deque()
                dq.append([start, 1])  # Start coloring the node with color 1
                vis[start] = 1

                while dq:
                    node, colour = dq.popleft()

                    for neighbor in graph[node]:  # Iterate over adjacent nodes (adjacency list)
                        if vis[neighbor] == 0:  # If the neighbor is uncolored
                            vis[neighbor] = -colour  # Assign the opposite color
                            dq.append([neighbor, -colour])
                        elif vis[neighbor] == colour:  # If the neighbor has the same color, it's not bipartite
                            return False
        
        return True  # If no conflicts are found, the graph is bipartite
#Start by giving a colour to starting node and to all its adjacents give the opposing colour
#And continue; and keep doing this for i in range(len(graph)) incase graph is discoonnected.
#If adjacent elements are same, return False.