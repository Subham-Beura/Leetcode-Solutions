class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent=[i for i in range(n)]
        rank=[1 for _ in range(n)]

        def find(node):
            root=node
            while root!=parent[root]:
                parent[root]=parent[parent[root]]
                root=parent[root]
            return root

        def union(left,right):
            l,r=find(left),find(right)
            if l==r:
                return 0
            if rank[l]>=rank[r]:
                parent[r]=l
                rank[l]+=rank[r]
            else:
                parent[l]=r
                rank[r]+=rank[l]
            return 1
        clusters=n
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    clusters-=union(r,c)
        return clusters






        