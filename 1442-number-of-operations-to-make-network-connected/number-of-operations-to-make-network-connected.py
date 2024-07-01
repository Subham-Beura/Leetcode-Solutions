class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            parent[p2] = p1
            return True
        
        # Strategy:
        # Count uneeded Edges
        #   where n1 and n2 are in same cluster
        # Count No of clusters
        # Check if we have enough to conn cluster
        uneededEdges = 0
        for n1, n2 in connections:
            if not union(n1, n2):
                uneededEdges += 1

        noOfCluster = len(set([find(i) for i in parent]))
        minEdgesForFullConnection = noOfCluster - 1
        if uneededEdges < minEdgesForFullConnection:
            return -1

        return noOfCluster - 1
