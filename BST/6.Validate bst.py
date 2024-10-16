# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,lower,higher):
            if node==None:
                return True
            if node.val<=lower or node.val>=higher:
                return False
            return helper(node.left,lower,node.val) and helper(node.right,node.val,higher)
        return helper(root,float('-inf'),float('inf'))

#Check if each node lies in the range.