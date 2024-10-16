# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[float('-inf')]
        def helper(root):
            if root==None:
                return 0 #maxsum thru one child side of the node
            l=helper(root.left)
            r=helper(root.right)

            thrusum=max(max(l,r)+root.val,root.val)#only either left or right tree
            maxisum=max(thrusum,root.val+l+r) #both left and right trees

            ans[0]=max(ans[0],maxisum)
            return thrusum
        helper(root)
        return ans[0]




            
        


            
#Here you probably don't need a helper function.
#store ans=[float(‘-inf’)] outside the function. 
# At each instance return maximum path sum starting with that node
# (either left+node or right+node or just node (incase negative)). 
# But also calculate  ans[0]  = max ( ans[0],node+left+right), but don't return it. Outside the helper function, call helper(root) , return ans[0]. 
