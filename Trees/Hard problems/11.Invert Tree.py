# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively call the invertTree function on the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
#recursively swap left and right nodes that's all.(Not on striver)