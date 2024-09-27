class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Find function with path compression
        def findroot(stone):
            if parent[stone] != stone:
                parent[stone] = findroot(parent[stone])
            return parent[stone]
        
        numnodes = 100000

        parent=list(range(numnodes*2))

        for x,y in stones:
            parent[findroot(x)]=parent[findroot(y+numnodes)]
        
        unique={findroot(x) for x,_ in stones}

        return len(stones)-len(unique)
#DSU, here logic is to assign parent of x to parent[y+100000] (so as to not have index error)
#If same x, there will be same parent and ofc if same y there will be same parent.
#The value 100k is chosen according to max 1000 stones, and testcases passing.