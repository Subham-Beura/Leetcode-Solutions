class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        totalProd=1
        noOfZeros=0
        for a in nums:
          if a==0:
            noOfZeros+=1
            continue
          totalProd*=a
        if noOfZeros>1:
          return [0]*len(nums)
        res=[]
        if noOfZeros==1:
          for a in nums:
            if a==0:
              res.append(totalProd)
              continue
            res.append(0)
          return res
        for a in nums:
          if a!=0:
            res.append(totalProd/a)
        return res