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
        
        def coursePossible(src):
          # Already done 
          if visited[src]==1:
            return True
          # Cycle!!! 
          if visited[src]==-1:
            return False
          visited[src]=-1
          for n in graph[src]:
            if not coursePossible(n):
              return False
          visited[src]=1
          return True

        for i in xrange(numCourses):
          if not coursePossible(i):
            return False
        return True
        
          