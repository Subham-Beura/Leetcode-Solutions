class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        candidates.sort()
        def dfs(i,path,currSum):
            if  currSum==target:
                res.append(path)
                return
            if i>=n or  currSum>target:
                return
            dfs(i+1,path+[candidates[i]],currSum+candidates[i])
            old=candidates[i]
            while(i+1<=len(candidates) and candidates[i]==old ):
                i+=1
            dfs(i,path,currSum)

        dfs(0,[],0)
        return res
