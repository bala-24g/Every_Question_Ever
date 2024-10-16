# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev=None
        big=None
        small=None

        def inorder(node):
            nonlocal small,big,prev
            if node==None:
                return 
            inorder(node.left)
            if prev and prev.val>node.val:
                small=node
                if not big:
                    big=prev
            prev=node
            inorder(node.right)
        inorder(root)
        small.val,big.val=big.val,small.val

        """
        Do not return anything, modify root in-place instead.
        """
        
#Inorder traversal in a bst: ascending order.
#Keep a prev, big and small node.
#If while doing inorder traversal, the prev value is greater than the current node value
#The previous value is the big node and the current value is the small node 
#Assign prev to the current node and call the inorder for the right too.
#Then swap the small and big values.
#Also , the big node once determined does not change, but the small node can.So keep that in mind.
#when writing the conditional loop.