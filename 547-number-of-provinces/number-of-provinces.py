class Solution:
    visited=set()
    def exploreAll(self,V,adj):
        if V in self.visited:
            return
        self.visited.add(V)
        for i in range(len(adj[0])):
            if adj[V][i]==1 and i not in self.visited:
                self.exploreAll(i,adj)
    def findCircleNum(self, adj: List[List[int]]) -> int:
        res=0
        self.visited=set()
        n=len(adj)
        for i in range(n):
            if i not in self.visited:
                res+=1
                self.exploreAll(i,adj)
        return res
