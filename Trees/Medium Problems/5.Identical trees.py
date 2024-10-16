# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p and q:
            return(p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        else:
            return False
        
#Check if nodes are same and left and right trees are same.