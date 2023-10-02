class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        def dfs(i,cur,total):
          if total==target:
            cur.sort()
            res.append(cur) 
            return 
          if total >=target or i>=len(candidates):
            return 
          
          dfs(i+1,cur+[candidates[i]],total+candidates[i])
          old=candidates[i]
          while(i+1<=len(candidates) and candidates[i]==old ):
            i+=1
          dfs(i,cur,total)
        
        dfs(0,[],0)


        # return s
        return res