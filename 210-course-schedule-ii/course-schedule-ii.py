class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Set up preq graph
        if not prerequisites:
            return range(numCourses)
        G={i:[] for i in range(numCourses)}
        preqs=[0 for _ in range(numCourses)]
        for c,p in prerequisites:
            preqs[c]+=1
            G[p].append(c)
        Q=deque()
        
        for c,nP in enumerate(preqs):
            # print(f"{c} {nP}")
            if nP==0:
                Q.append(c)
        # print(G)
        # print(preqs)
        # print(Q)
        topo=[]
        while Q:
            # print(Q)
            node=Q.popleft()
            topo.append(node)
            for n in G[node]:
                preqs[n]-=1
                if preqs[n]==0:
                    Q.append(n)
        return topo if len(topo)==numCourses else []

        