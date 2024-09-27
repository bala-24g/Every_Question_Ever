from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Helper function to perform BFS
        def cycle(src, vis):
            dq = deque()
            dq.append([src, -1])  # Start with source node and parent as -1
            
            while dq:
                node, parent = dq.popleft()
                
                if vis[node]:  # If the node is already visited
                    return True  # Cycle detected
                
                vis[node] = True  # Mark the node as visited
                
                # Check all adjacent nodes
                for nei in adj[node]:
                    if not vis[nei]:  # If neighbor is not visited
                        dq.append([nei, node])  # Append neighbor and current node as parent
                    elif nei != parent:  # If neighbor is visited and not the parent, cycle detected
                        return True
            
            return False
        
        vis = [False] * V  # To track visited nodes
        
        # Loop through each node (to handle disconnected components)
        for i in range(V):
            if not vis[i]:  # Check if the node is not visited
                if cycle(i, vis):  # Start BFS if the node is not visited
                    return True  # Cycle found
        
        return False  # No cycle found
#Have a helper function, accepting src and visited array as parameters
#Push src,-1 (node, parent ) into the dq.
#Then popleft the node,parent; and if the node is visited return True.
#Else, mark the node as visited.
#Then for nei in adj of nodes, if nei is not visited push it into queue.
#If nei is visited and nei is not parent return True

#Now, in main; instantiate visted with all Falses
#For i in range(V), if vis[i]==False and helper(i,vis)==True: return true
#After all iterations, return False