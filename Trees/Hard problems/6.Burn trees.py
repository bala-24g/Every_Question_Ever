class Solution:
    def minTime(self, root,target):
        #set parent for each one
        #Traverse till size(visited)=number of nodes in binary trees
        
        dq=deque()
        dq.append([root,root])
        
        parentlist={}
        targetnode=None
        while dq:
            node,parent=dq.popleft()
            parentlist[node]=parent
            if node.data==target:
                targetnode=node
                
            if node.left:
                dq.append([node.left,node])
            if node.right:
                dq.append([node.right,node])
        
        dq.append([targetnode,0])
        visited=set()
        maxtime=0
        while dq:
            node,time=dq.popleft()
            maxtime=max(time,maxtime)
            visited.add(node)
            if node.left and node.left not in visited:
                dq.append([node.left,time+1])
            if node.right and node.right not in visited:
                dq.append([node.right,time+1])
            if parentlist[node] not in visited:
                dq.append([parentlist[node],time+1])
        return maxtime
#Parent mapping then start pushing into the queue from the target node