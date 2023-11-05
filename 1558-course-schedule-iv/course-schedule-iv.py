class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        INF=999999999
        graph=[[False]*numCourses for _ in xrange(numCourses)]

        for crs,preq in prerequisites:
          graph[crs][preq]=True
        for k in xrange(numCourses):
          for src in xrange(numCourses):
            for dest in xrange(numCourses):
              graph[src][dest]=graph[src][dest] or (graph[src][k] and graph[k][dest])
        res=[]
        for src,dest in queries:
          res.append(graph[src][dest])
        return res
