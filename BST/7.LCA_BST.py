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
            lefttree=helper(node.left)
            righttree=helper(node.right)
            if lefttree and righttree:
                return node
            if lefttree!=None:
                return lefttree
            else:
                return righttree
        return helper(root)

    #Same as LCA in tree.