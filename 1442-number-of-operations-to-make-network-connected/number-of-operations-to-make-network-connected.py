class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[1]*(n)
        def find(x):
            p=parent[x]

            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            parent[x]=p
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            
            if p1==p2:return False

            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        uneededEdges=[]
        for n1,n2 in connections:
            # noOfCluster=len(set(parent))
            u=union(n1,n2)
            # print(u)
            if not u :
                uneededEdges.append((n1,n2))
        for i in range(n):
            find(i)
        noOfCluster=len(set(parent)) 
        # print(uneededEdges)
        # print(noOfCluster)
        if len(uneededEdges)<noOfCluster-1:
            return -1
        
        return noOfCluster-1