class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        counter=Counter(arr1)
        res=[0]*(len(arr1))
        count=0
        for n in arr2:
            for c in range(counter[n]):
                res[count]=n
                count+=1
            counter[n]=0
        counter=dict(sorted(counter.items()))
        for k,v in counter.items():
            for c in range(v):
                 res[count]=k
                 count+=1
        return res 
        