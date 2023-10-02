class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res=[]
        if nums==[]:
          return None
        n=len(nums[0])

        def dfs(i,cur):
          if len(cur)==n:
            if cur not in nums:
              res.append(cur)
            return 
          if len(cur)>n:
            return 

          dfs(i+1,cur+'0')
          if len(res) !=0:
            return 
          dfs(i+1,cur+'1') 
          if len(res)!= 0:
            return 
        dfs(0,"")
        return res[0]