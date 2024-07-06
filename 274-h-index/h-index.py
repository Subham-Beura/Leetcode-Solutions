class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)<=1:
            return 1 if citations[0]>0 else 0
        citations.append(float("inf"))
        citations.sort(key=lambda x:-1*x)
        # print(citations)
        for i in range(1,len(citations)):
            # print(f"{i} {citations[i]}")
            if i>citations[i]:
                return i-1
        return  len(citations)-1
        