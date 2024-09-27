# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        
        curlevel=[]
        nextlevel=[]
        curlevel.append(root)
        lefttoright=True
        temp=[]

        while curlevel:
            size=len(curlevel)
            while size>0:
                size-=1
                top=curlevel.pop()
                temp.append(top.val)
                if lefttoright:
                    if top.left:
                        nextlevel.append(top.left)
                    if top.right:
                        nextlevel.append(top.right)
                else:
                    if top.right:
                        nextlevel.append(top.right)
                    if top.left:
                        nextlevel.append(top.left)
            curlevel,nextlevel=nextlevel,curlevel
            lefttoright=not(lefttoright)
            ans.append(temp)
            temp=[]
        return ans

        
#Level wise traversal, so have a while loop and size of stack while loop inside that also.
#The temp is there just to format the answer correctly.