class Solution:
    def bottomView(self, root):
        # code here
        if root==None:
            return []
        ans=[]
        dq=[]
        dictt={}
        
        dq.append([root,0])
        while dq:
            node,lvl=dq.pop(0)
            dictt[lvl]=node.data
            if node.left:
                dq.append([node.left,lvl-1])
            if node.right:
                dq.append([node.right,lvl+1])
        
        for i in sorted(dictt.keys()):
            ans.append(dictt[i])
        return ans
#Same as before, but here even if the ith level is already visited in dictionary you have to replace it with the latest seen one.