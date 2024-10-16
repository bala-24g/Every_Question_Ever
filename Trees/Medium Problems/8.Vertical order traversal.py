from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dictt = defaultdict(list)
        queue = [(root, 0, 0)]  # Use a tuple (node, vertical level, depth)

        while queue:
            node, lvl, depth = queue.pop(0)
            dictt[lvl].append((depth, node.val))  # Collect by (depth, value)
            if node.left:
                queue.append((node.left, lvl - 1, depth + 1))
            if node.right:
                queue.append((node.right, lvl + 1, depth + 1))

        ans = []
        
        for lvl in sorted(dictt.keys()):
            # Sort the values at the same vertical level by depth, then by value
            temp = sorted(dictt[lvl], key=lambda x: (x[0], x[1]))
            ans.append([val for _, val in temp])  # Append only values
        
        return ans
#Use a bfs, and maintain a dictionary for the vertical level. Then for each lvl in dictionary as the key, append by the depth, value pairs. Then add to answer by sorting with depth first then by values.