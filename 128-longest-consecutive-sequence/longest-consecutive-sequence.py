class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet=set(nums)

        res=0

        for n in numSet:
            if n-1 not in numSet:
                l=0
                while n+l in numSet:
                    l+=1
                res=max(res,l)
        return res
                


        