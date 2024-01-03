class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n=len(nums1)
        m=len(nums2)
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        res=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                    res=max(res,dp[i][j])
        return res
        