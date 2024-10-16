from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: BFS to create a parent map and locate the target node
        parentmap = {}
        dq = deque([root])
        needed = None
        
        while dq:
            node = dq.popleft()
            
            # Record parent-child relationships
            if node.left:
                parentmap[node.left] = node  # Map the child node to its parent
                dq.append(node.left)
            if node.right:
                parentmap[node.right] = node  # Map the child node to its parent
                dq.append(node.right)
        
        # Step 2: BFS to find all nodes at distance K from the target
        dq = deque([(target, 0)])  # (node, distance from target)
        visited = set([target])  # Keep track of visited nodes to avoid cycles
        ans = []
        
        while dq:
            node, dist = dq.popleft()
            
            if dist == k:
                ans.append(node.val)  # If the current node is at distance K, add to result
            elif dist > k:
                break  # No need to explore further if distance exceeds K
            
            # Explore left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                dq.append((node.left, dist + 1))
            
            # Explore right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                dq.append((node.right, dist + 1))
            
            # Explore parent (if exists and not visited)
            if node in parentmap and parentmap[node] not in visited:
                visited.add(parentmap[node])
                dq.append((parentmap[node], dist + 1))
        
        return ans
#Traverse and maintain parent-child relationships
#Then go from the target,mark visited and keep track of distance.