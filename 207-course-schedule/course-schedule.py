class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preq={}
        for n in range(numCourses):
          preq[n]=[]
        for crs,pre in prerequisites:
          preq[crs].append(pre)
        visited=set()
        def dfs(n):
          if n in visited:
            return False
          if preq[n] == []:
            return True
          visited.add(n)
          for c in preq[n]:
            if not dfs(c): return False
          visited.remove(n)
          preq[n]=[]
          return True
        for n in range(numCourses):
          if not dfs(n): return False
        return True
          