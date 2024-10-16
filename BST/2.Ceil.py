#Function to return the ceil of given number in BST.
class Solution:
    def findCeil(self, root, inp):
        # Initialize target as -1, meaning no ceil found
        target = -1
        
        def helper(root):
            nonlocal target
            if root is None:
                return
            if root.data == inp:  # If exact match found
                target = root.data
                return
            if root.data > inp:  # Potential ceil, check left for smaller valid value
                target = root.data
                helper(root.left)
            else:  # If smaller, move to the right subtree
                helper(root.right)
        
        helper(root)
        return target
