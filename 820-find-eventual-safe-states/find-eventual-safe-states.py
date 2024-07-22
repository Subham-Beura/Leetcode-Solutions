class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        G={i:[] for i in range(len(graph))}
        inDeg=[0]*(len(graph))
        for s,neis in enumerate(graph):
            for d in neis:
                G[d].append(s)
            inDeg[s]=len(neis) 
        # print(G)
        # print(inDeg)      
        q=deque([i for i,inD in enumerate(inDeg) if inD==0 ])
        topo=[]
        while q:
            node=q.popleft() 
            topo.append(node)
            for n in G[node]:
                inDeg[n]-=1
                if inDeg[n]==0:
                    q.append(n)
        return sorted(topo)