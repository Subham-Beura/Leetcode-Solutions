class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        greed.sort()
        sizes.sort()
        sorted_child=0
        i=0
        for child in greed:
            while i<len(sizes) and child >sizes[i] :
                i=i+1
            if i==len(sizes):
                break
            sorted_child+=1  
            i=i+1
        return sorted_child

        
