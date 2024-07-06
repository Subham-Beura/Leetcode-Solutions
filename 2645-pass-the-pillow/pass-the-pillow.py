class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction=1
        i=0
        for t in range(0,time+1):
            if i==n:
                direction=-1
            if i==1:
                direction=1
            i+=1*direction
            print(i)
        return i
            

