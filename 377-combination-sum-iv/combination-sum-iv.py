class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[-1]*(target+1)
        def finder(target):
            if target<0:
                return 0
            if target==0:
                return 1
            if dp[target] !=-1:
                return dp[target]
            totalWays=0
            for n in nums:
                totalWays+=finder(target-n)

            dp[target]= totalWays
            return totalWays
        return finder(target)

        