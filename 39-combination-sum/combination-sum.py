class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        def dfs(i,path,currSum):
            if currSum>target:
                return 
            if i==n and currSum!=target:
                return
            if i==n:
                res.append(path)
                return
            dfs(i,path+[candidates[i]],currSum+candidates[i]) 
            dfs(i+1,path,currSum) 

        dfs(0,[],0)
        return res