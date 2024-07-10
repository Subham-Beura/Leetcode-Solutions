class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for cmd in logs:
            if cmd=='./':
                continue
            elif cmd=="../":
                count-=1
                count=max(0,count)
            else:
                count+=1
        return count
            