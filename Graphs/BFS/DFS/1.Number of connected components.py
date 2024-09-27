class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis=[False]*len(isConnected)

        count=0
        n=len(isConnected)

        def helper(node):
            for neighbour in range(n):
                if isConnected[node][neighbour]==1 and not vis[neighbour]:
                    vis[neighbour]=True
                    helper(neighbour)
        for i in range(n):
            if not vis[i]:
                vis[i]=True
                helper(i)
                count+=1
        return count


            
                
                
#NEED:visited array
#Go one by one to the nodes, and traverse to their available connections. Each time you 
#go to a new node, only go if it hasn't already been visited. If it hasn't, mark it visited and 
#add it to count.