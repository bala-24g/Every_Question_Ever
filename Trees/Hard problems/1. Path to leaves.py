from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        path=[]
        ans=[]
        def lol(root,path,ans):
            if root is None:
                return
            else:
                path.append(root.data)
                if root.left:
                    lol(root.left,list(path),ans)
                if root.right:
                    lol(root.right,list(path),ans)
                if not root.left and not root.right:
                    ans.append(path)
                
        lol(root,path,ans)
        return ans
#If order does not matter, problem is easier (see failed gfg submissions from me)
#But order matters, so you have to use dfs.
#If root==None: return , else add the node value to list, then call recursively for left and right (create copies and call/append). If neither left or right, then just append the path to ans.