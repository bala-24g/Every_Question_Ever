# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l,r):
            if l==None and r==None:
                return True
            if l==None and r!=None:
                return False
            if l!=None and r==None:
                return False
            if l.val!=r.val:
                return False
            return helper(l.left, r.right) and helper(l.right, r.left)
        return helper(root.left,root.right)
#Check recursively left and right trees