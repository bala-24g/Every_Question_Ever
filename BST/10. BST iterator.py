# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.inorder(root)
    def inorder(self,node):
        while node:
            self.stack.append(node)
            node=node.left
        


    def next(self) -> int:
        topnode=self.stack.pop()

        if topnode.right:
            self.inorder(topnode.right)
        return topnode.val


    def hasNext(self) -> bool:
        return (len(self.stack)>0)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#Initialise stack, call inorder of all left, then pop stack and if right call inorder of the right and return the last value on the left of the right
#Then finally return if stack is not empty.