class Solution:
    def floor(self, root, x):
        # Code here
        target=-1
        def helper(node):
            nonlocal target
            if node==None:
                return
            if node.data==x:
                target=node.data
                return
            if node.data<x:
                target=node.data
                helper(node.right)
            else:
                helper(node.left)
        helper(root)
        return target
#Same as b4

                