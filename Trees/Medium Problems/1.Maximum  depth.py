# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        ldepth=self.maxDepth(root.left)
        rdepth=self.maxDepth(root.right)
        return(max(ldepth,rdepth)+1)
#Recursion: if the root is none, return 0.
#Else return the max of left+right+1
