class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=[g-c for g,c in zip(gas,cost)]
        if sum(diff)<0:
            return -1
        total=0
        start=0
        for i,diff in enumerate(diff):
            total+=diff
            if total<0:
                total=0
                start=i+1
        return start
    