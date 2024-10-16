#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def check_sum(root):
            if root is None:
                return True
            
            if root.left is None and root.right is None:
                return True
            
            left_data=0
            right_data=0
            
            if root.left:
                left_data= root.left.data
            
            if root.right:
                right_data = root.right.data
            
            if root.data==left_data+right_data:
                return check_sum(root.left) and check_sum(root.right)
                
            else:
                return False
        return 1 if check_sum(root) else 0
#See if at each node the sum property is satisfied. Check base cases (root is None OR root has no children)
#Then check if left and right exist if they do store their values and check if the current node's value is same as the sum of left and right
#If it is then check recursively
#Else return False