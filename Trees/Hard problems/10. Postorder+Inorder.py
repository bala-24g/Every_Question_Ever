# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        index=len(postorder)-1

        def helper(inStart,inEnd):
            nonlocal index

            if inStart>inEnd:
                return None
            Node=TreeNode(postorder[index])
            index-=1
            if inStart==inEnd:
                return Node
            iIndex=mapp[Node.val]

            Node.right = helper(iIndex + 1, inEnd)
            Node.left = helper(inStart, iIndex - 1)
            
            
            return Node
        return helper(0,len(postorder)-1)
        

            
    #7.Build from postorder and inorder: (Very similar to prev one) 
    # Here also build a map for inorder (value vs index), then keep a track of the postorder index 
    # (nonlocal within the helper function) (starting from len(postorder-1)) ofc check if inStart>inEnd and 
    # return 0, else create a node with the postorder index , and decrement postorder index. If the inStart==inEnd, return Node. Else, get the inorder index of the new Node.val, 
    # build the right and left subtree (IN PREV IT WAS LEFT AND RIGHT SUBTREE). Left subtree= helper(inStart,NodeIndex-1), Right subtree=helper(NodeIndex+1,inEnd).