class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        def dfs(i,path):
            if i>=n:
                res.append(path)
                return
            dfs(i+1,path+[nums[i]])
            old=nums[i]
            while(i+1<n and nums[i+1]==old):
                i+=1
            dfs(i+1,path)
        dfs(0,[])
        return res