# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=TreeNode(preorder[0])
        stack=[]
        stack.append(root)
        for i in range(1,len(preorder)):
            parent=stack[-1]
            child=TreeNode(preorder[i])
            while stack and stack[-1].val<child.val:
                parent=stack.pop()
            if parent.val>child.val:
                parent.left=child
            else:
                parent.right=child
            stack.append(child)
        return root


#Push root node into stack, for i in range(1,n): create parent as top of stack and child as preorder[i]
#Then while stack, and stack[-1].val<child.val (i.e go till you find parent)
#keep popping, then if parent.val>child.val attach child to left else to right of parent.
#Then stack.append child. 
#Outside while loop return root

        