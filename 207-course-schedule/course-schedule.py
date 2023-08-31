class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visitSet=set()
        preq={i:[] for i in range(numCourses)}

        for crs,prq in prerequisites:
          preq[crs].append(prq)


        def dfs(crs):
          if crs in visitSet:
            return False
          if preq[crs]==[]:
            return True
          visitSet.add(crs)
          for i in preq[crs]:
            if not dfs(i) : return False
          preq[crs]=[]
          visitSet.remove(crs)
          return True
        for i in range(numCourses):
          if not dfs(i): return False
        return True