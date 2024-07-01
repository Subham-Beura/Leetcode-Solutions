class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for n in arr:
            if count==3:
                return True
            
            if n&1==1:
                count+=1
            else:
                count=0
            
        return count==3