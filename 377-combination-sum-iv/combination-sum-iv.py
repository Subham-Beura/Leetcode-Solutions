class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[-1]*(target+1)
        def ans(nums,t):
          if t==0:
            return 1
          if t<0: 
            return 0
          if dp[t] !=-1:
            return dp[t]
          res=0
          for num in nums:
             res+=ans(nums,t-num)
          dp[t]=res
          return res
        return ans(nums,target)