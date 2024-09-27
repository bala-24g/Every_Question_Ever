class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def findroot(computer):
            if parent[computer]!=computer:
                parent[computer]=findroot(parent[computer])
            return parent[computer]
        spare=0
        parent=[0]*n

        for i in range(n):
            parent[i]=i
        
        for a,b in connections:
            roota=findroot(a)
            rootb=findroot(b)
            if roota==rootb:
                spare+=1
            else:
                parent[roota]=rootb
                n-=1
        if n-1>spare:
            return -1
        else:
            return n-1

        

        
            
#Using disjoint set you have to attach parents to each. 