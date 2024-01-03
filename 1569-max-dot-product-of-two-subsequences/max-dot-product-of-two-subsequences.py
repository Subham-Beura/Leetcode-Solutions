class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n=len(nums1)
        m=len(nums2)
        dp=[[0]*(m) for _ in range(n)]
        dp[0][0]=nums1[0]*nums2[0]
        for i in range(1,n):
            if nums1[i]*nums2[0]>=dp[i-1][0]:
                dp[i][0]=nums1[i]*nums2[0]
            else:
                dp[i][0]=dp[i-1][0]

        for c in range(1,m):
            if nums1[0]*nums2[c]>=dp[0][c-1]:
                dp[0][c]=nums1[0]*nums2[c]
            else:
                dp[0][c]=dp[0][c-1]

        for i in range(1,n):
            for j in range(1,m):
                # Add
                bothSide=dp[i-1][j-1]+nums1[i]*nums2[j]
                dp[i][j]=max(bothSide,dp[i-1][j],dp[i][j-1],nums1[i]*nums2[j])
        print(dp)
        return dp[n-1][m-1]