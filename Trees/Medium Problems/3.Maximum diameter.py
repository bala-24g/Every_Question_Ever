# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root==None:
                return(0,0) #height,diameter
            lht,ldia=helper(root.left)
            rht,rdia=helper(root.right)

            dia=max(lht+rht,max(ldia,rdia))
            ht=max(rht,lht)+1
            return(ht,dia)
        _,dia=helper(root)
        return dia
    
#3.Calculate diameter-> Like last question, where you have to keep track of height and left and right diameters, In a post order fashion-> i.e  defining a helper function, then the base case returns then how to process with the base case returns for the subsequent cases, then outside the helper function returning what we want from the helper function(i.e choosing the diameter only since the helper function is keeping track of height and diameter). 
#These types of qns the thing is to keep track of the ans in the second variable and what the ans depends on in the first variable and use a helper function to see both.