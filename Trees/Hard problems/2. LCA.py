# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node==None:
                return None
            if node.val==p.val or node.val==q.val:
                return node

            leftnode=helper(node.left)
            rightnode=helper(node.right)

            if leftnode and rightnode:
                return node
            
            if leftnode!=None:
                return leftnode
            else:
                return rightnode
        return helper(root)
#Check if the node reached is either p or q
#Else, go to left and right and check if they have p or q.
#If both left and right are not None (i.e; they have one of each OR if one is a descendant of other in left or right)
#If letftnode has one then return it, else return rightnode.(Whichever is not None it returns that)