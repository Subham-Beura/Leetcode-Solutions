class Solution:
    visited=set()
    # res=deqeue()
    path=[]
    def dfs(self,node,G):
        
        self.visited.add(node)
        if node in self.path:
            return False
        self.path.append(node)
        for crs in G[node]:
            if crs in self.path:
                print(node)
                return False
            if crs in self.visited:
                continue
            if not self.dfs(crs,G):
                return False
        self.path.remove(node)
        return True



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Set up preq graph
        if  len(prerequisites)<2:
            return True

        self.visited=set()
        self.path=[]
        G=[[] for _ in range(numCourses)]
        
        for crs,preq in prerequisites:
            G[preq].append(crs)
        print(G)
        for i in range(numCourses):
            if i in self.visited:
                continue
            if not self.dfs(i,G):
                return False
        return True