class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x:-1*x)
        for i in range(0,len(citations)):
            # print(f"{i} {citations[i]}")
            if i+1>citations[i]:
                return i
        return  len(citations)
        