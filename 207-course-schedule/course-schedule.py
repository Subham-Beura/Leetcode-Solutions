class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=[[] for _ in xrange(numCourses)]
        visited=[0 for _ in xrange(numCourses)]

        for crs,preq in prerequisites:
          graph[crs].append(preq)
        
        def dfs(src):
          if visited[src]==1:
            return True
          if visited[src]==-1:
            return False
          visited[src]=-1
          for preq in graph[src]:
            if not dfs(preq):
              return False
          visited[src]=1
          return True
        for i in range(numCourses):
          if not dfs(i):
            return False
        return True
          
        
          