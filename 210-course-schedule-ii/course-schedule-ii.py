class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph=[[] for _ in xrange(numCourses)]
        visited=[0 for _ in xrange(numCourses)]

        res=[]

        # make adj
        for crs,preq in prerequisites:
          graph[crs].append(preq)

        def dfs(src):
          if visited[src]==-1:
            return False
          if visited[src]==1:
            return True
          visited[src]=-1
          for preq in graph[src]:
            if not dfs(preq):
              return False
          visited[src]=1
          res.append(src)
          return True



        for crs in xrange(numCourses):
          if not dfs(crs):
            return []
        return res
        