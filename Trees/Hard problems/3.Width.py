# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq=deque()
        dq.append([root,0])
        maxlen=0

        while dq:
            lvl=len(dq)
            
            node,firstindex=dq[0]

            while lvl:
                lvl-=1
                node,index=dq.popleft()
                norm=index-firstindex

                if node.left:
                    dq.append([node.left,2*norm])
                if node.right:
                    dq.append([node.right,2*norm+1])
                if lvl==0:
                    maxlen=max(maxlen,norm+1)
        return maxlen
#Use normalised index and add to the next levels.