class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if root==None:
            return []
        ans=[]
        dq=[]
        dictt={}
        
        dq.append([root,0])
        while dq:
            node,lvl=dq.pop(0)
            if lvl not in dictt.keys():
                dictt[lvl]=node.data
            if node.left:
                dq.append([node.left,lvl-1])
            if node.right:
                dq.append([node.right,lvl+1])
        
        for i in sorted(dictt.keys()):
            ans.append(dictt[i])
        return ans
#Very similar to last one but you need not use depth. And each dictionary key needs to store only one value.