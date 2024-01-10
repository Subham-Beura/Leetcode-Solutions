class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n
        dp[0]=nums[0]
        if n==1:
            return nums[0]
        dp[1]=max(nums[0],nums[1])
        if n==2:
            return dp[1]
        res=-1
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            res=max(res,dp[i])

        return res