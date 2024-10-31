class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        G=collections.defaultdict(list)
        for s,d in connections:
            G[s].append(d)
            G[d].append(s)
        visited=set()

        def dfs(src):
            if src in visited:
                return False
            visited.add(src)
            for n in G[src]:
                if n not in visited:
                    dfs(n)
            return True
        
        no_of_clusters=0
        for i in range(n):
            if dfs(i):
                no_of_clusters+=1
        return no_of_clusters-1
                