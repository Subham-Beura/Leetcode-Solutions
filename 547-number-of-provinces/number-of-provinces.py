class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        G=collections.defaultdict(list)

        for s in range(n):
            for d in range(n):
                if isConnected[s][d]:
                    G[s].append(d)
        
        visited=set()

        provinces=0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for n in G[node]:
                if n not in visited:
                    dfs(n)
            return True

        for i in range(n):
            if dfs(i):
                provinces+=1
        return provinces



        