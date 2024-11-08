class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==1:
            return nums
        cache=[1]*(n)
        prev=[-1]*(n)
        max_i=0
        max_v=-1
        nums.sort()
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if (nums[j]%nums[i]==0 ) and cache[i]<=cache[j]+1:
                    cache[i]=cache[j]+1
                    prev[i]=j
            if max_v<cache[i]:
                max_v=cache[i]
                max_i=i
        res=[]
        print(cache)
        for i in range(max_v):
            res.append(nums[max_i])
            max_i=prev[max_i]

        return res