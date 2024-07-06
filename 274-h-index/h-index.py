class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        count=[0]*(n+1)
        for c in citations:
            count[min(c,n)]+=1
        citations=[]
        for i in range(n,-1,-1):
            for j in range(count[i]):
                citations.append(i)

        for i in range(n):
            # print(f"{i} {citations[i]}")
            if i+1>citations[i]:
                return i
        return  len(citations)
        