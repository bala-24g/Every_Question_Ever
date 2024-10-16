# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=[]
        def inorder(node):
            nonlocal arr
            if node==None:
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        x=0
        y=len(arr)-1

        while x<y:
            if (arr[x]+arr[y]<k):
                x+=1
            elif (arr[x]+arr[y]>k):
                y-=1
            elif (arr[x]+arr[y]==k):
                return True
        return False
    #Get inorder traversal and do binary search.