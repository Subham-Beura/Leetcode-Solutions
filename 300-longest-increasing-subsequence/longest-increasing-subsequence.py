class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*(n)
        
        if n==1 or n==1:
            return n
        res=0
        for i in range(n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            res=max(res,dp[i])        
        return res

        