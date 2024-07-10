class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for cmd in logs:
            if cmd=='./':
                continue
            elif cmd=="../":
                if count==0:
                    continue
                count-=1
            else:
                count+=1
        return count
            