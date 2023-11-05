class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        INF=999999999
        graph=[[INF]*numCourses for _ in xrange(numCourses)]

        for crs,preq in prerequisites:
          graph[crs][preq]=1
        for k in xrange(numCourses):
          for src in xrange(numCourses):
            for dest in xrange(numCourses):
              graph[src][dest]=min(
                graph[src][dest],
                graph[src][k]+graph[k][dest]
              )
        res=[]
        for src,dest in queries:
          if graph[src][dest]==INF:
            res.append(False)
            continue
          res.append(True)
        return res
