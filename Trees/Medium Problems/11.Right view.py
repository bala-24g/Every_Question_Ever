# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        dq=[]
        dq.append([root,0])
        dictt={}
        
        while dq:
            node,lvl=dq.pop(0)
            if lvl not in dictt.keys():
                dictt[lvl]=node.val
            if node.right:
                dq.append([node.right,lvl+1])
            if node.left:
                dq.append([node.left,lvl+1])
        ans=[]
        for i in sorted(dictt.keys()):
            ans.append(dictt[i])
        return ans      
#Very similar to prev logic, except the levels are always incremented , not dec for left and inc for right; and also first seen at each level is recorded in dictionary.