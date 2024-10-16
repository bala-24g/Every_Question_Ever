#User function Template for python3
class Solution:
    def largestBst(self, root):
    
        maxsize=0
        
        def helper(node):
            nonlocal maxsize
            if node==None:
                return True,0,float('inf'),float('-inf')
                
            isleft,leftsize,leftlower,leftupper=helper(node.left)
            isright,rightsize,rightlower,rightupper=helper(node.right)
            
            if isleft and isright and leftupper < node.data < rightlower:
                size=1+leftsize+rightsize
                maxsize=max(maxsize,size)
                
                return True,size,min(leftlower,node.data),max(rightupper,node.data)
            else:
                return False,0,0,0
                
            
            
               
        helper(root)
        return maxsize
                        
#Each tree is a bst if node is greater than max of left subtree and lesser than min of right subtree
#You have to use this to determine if a tree is a bst or not
#Then you have to keep track of min value of each tree and max value of each tree 
#Go till you reach None, if None has been reached then it's a bst.
#And set min and max values each time you recursively call the trees.