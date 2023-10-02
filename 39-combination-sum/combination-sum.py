class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(i,cur,total):
          if total==target:
            res.append(cur)
            return 
          if i >= len(candidates) or total> target:
            return 
          
          dfs(i,cur+[candidates[i]],total+candidates[i])
          dfs(i+1,cur,total)
        dfs(0,[],0)
        return res