class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minv=9999999
        for i in range(len(nums)):
          if nums[i]<0:
            nums[i]=0
          elif nums[i]<minv and nums[i]>0:
            minv=nums[i]
        if minv>1:
          return 1
        
        for i in range(len(nums)):
          val=abs(nums[i])
          if 1<=val<=len(nums):
            if nums[val-1] >0:
              nums[val-1]*=-1
            if nums[val-1]==0:
              nums[val-1]=(len(nums)+1)*-1
        for i in range(1,len(nums)+1):
          if nums[i-1]>=0:
            return i
        return len(nums)+1