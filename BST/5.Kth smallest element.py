# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        while root:
            stack.append(root)
            root=root.left
        for i in range(k-1):
            root=stack.pop()
            while root:
                root=root.right
                while root:
                    stack.append(root)
                    root=root.left
        return(stack[-1].val)
                

#Push all the left elements, then pop one by one, and go right then push each of their lefts
#into the stack too.
