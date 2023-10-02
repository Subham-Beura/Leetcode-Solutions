class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        n=len(nums)
        def dfs(i,cur):
          if i==n:
            res.append(cur) 
            return
          if i>=n:
            return
          # Take It
          dfs(i+1,cur+[nums[i]])
          # Ignore all other of this kind
          old=nums[i]
          while i<len(nums) and nums[i]==old:
            i+=1
          dfs(i,cur)
        dfs(0,[])
        return res