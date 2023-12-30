class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[0]*(n+1)
        for i in nums:
            if dp[i]==1:
                return i
            dp[i]+=1
        return 0
        