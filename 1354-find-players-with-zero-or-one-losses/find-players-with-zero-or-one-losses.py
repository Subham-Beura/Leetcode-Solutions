class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set([x[0] for x in matches]+[x[1] for x in matches])
        winner=[x[0] for x in matches]
        losers=[x[1] for x in matches]
        lossCount=Counter(losers)
        res=[[],[]]
        for k in players:
            losses=lossCount.get(k,0)
            if lossCount.get(k,0)==1:
                res[1].append(k)
            if losses==0 and k in players:
                res[0].append(k)
        res[0].sort()
        res[1].sort()
        return res