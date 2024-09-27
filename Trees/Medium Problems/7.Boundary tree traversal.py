#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        def lefttraversal(root,l):
            if not root or (not root.left and not root.right):
                return
            l.append(root.data)
            if root.left:
                lefttraversal(root.left,l)
            else:
                lefttraversal(root.right,l)
            
           
        def righttraversal(root,r):
            if not root or (not root.left and not root.right):
                return 
            if root.right:
                righttraversal(root.right,r)
            else:
                righttraversal(root.left,r)
            
            r.append(root.data)
            
        def leavestraversal(root,leaves):
            if not root:
                return
            leavestraversal(root.left,leaves)
            if not root.left and not root.right:
                leaves.append(root.data)
            leavestraversal(root.right,leaves)
            
        l=[]
        r=[]
        leaves=[]
        
        if root.left or root.right:
            l.append(root.data)
        else:
            return[root.data]
        
        
        lefttraversal(root.left,l)
        righttraversal(root.right,r)
        leavestraversal(root,leaves)
        return(l+leaves+r)
#Left + leaves + right traversals. See the different functions and how they're called.