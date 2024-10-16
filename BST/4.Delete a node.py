# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return root

        def helper(node,value):
            if node==None:
                return node 
            if node.val>value:
               node.left= helper(node.left,value)
            elif node.val<value:
                node.right= helper(node.right,value)
            else:
                if node.right==None:
                    return node.left
                elif node.left==None:
                    return node.right
                else:
                    curr=node.right
                    while curr and curr.left:
                        curr=curr.left
                    node.val=curr.val
                    node.right=helper(node.right,curr.val)
            return node
           
                    
        return(helper(root,key))
        
        

                        
#Keep assigning left and right nodes according to the search value; and if the node
#Has been found, you delete it by going to its right tree and and finding the lowest value by
#going to the left and then assigning that value to the deleted node value, 
#Then the right of that node is just the helper(node.right,curr.val(WHICH IS The leftmost val, i.e you're moving up the leftmost in the right subtree to the deleted node position.))
#Return node inside the function.

#Return helper(root,key).