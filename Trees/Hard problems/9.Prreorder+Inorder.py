# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        preIndex=0
        def helper(inStart,inEnd):
            nonlocal preIndex
            if inStart>inEnd:
                return None
            curr=preorder[preIndex]
            preIndex+=1
            tNode=TreeNode(curr)
            if inStart==inEnd:
                return tNode
            inIndex=mapp[curr]
            tNode.left=helper(inStart,inIndex-1)
            tNode.right=helper(inIndex+1,inEnd)
            return tNode
        return helper(0,len(inorder)-1)

            
# You need to build a dictionary to keep indices of every element 
# in inorder.Define preorder index=0. 
# Then define a helper function (inStart,inEnd) with nonlocal preorder.
# If inStart>inOrder, return None. 
# Else, create a node with the preorder element pointed to by the 
# preorder index. Increment the preorder index. If inStart==inEnd, 
# return the newly created treeNode. Else, get the inorder index of 
# the newly created node, and recursively build the left subtree and right
# subtree with the instart to postorder index of the newly created node, 
# postorder index of newly created node+1, inEnd.





    
