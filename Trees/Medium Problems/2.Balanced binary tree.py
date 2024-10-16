# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root==None:
                return 0,True
            rht,right=helper(root.right)
            lht,left=helper(root.left)
            isBal=right and left and abs(rht-lht)<=1
            return max(rht,lht)+1,isBal
        _,res=helper(root)
        return res

#Return if left height and right height difference is atmost 1.
#We need to check two parameters: i.e are left and right trees balanced and if their heights to see if their difference is less than 1.
#This is unlike the prev maxdepth one because in maxdepth you just had to check which of left and right had max height.
