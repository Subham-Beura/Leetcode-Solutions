class Solution:
    def checkIfPossibleToday(self,i,bloomDay,noOfB,flowers):
        L,R=0,0
        while R<len(bloomDay):
            if bloomDay[R]>i:
                R+=1
                L=R
            elif R-L+1==flowers:
                noOfB-=1
                L=R+1
                R=L
            else:
                R+=1
        res=noOfB<=0
        # print(res)
        return res

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        L,R=1,max(bloomDay)
        ans=-1
        while L<=R:
            mid=(L+R)//2
            check_mid=self.checkIfPossibleToday(mid,bloomDay,m,k)
            # print(f"{L} {mid} {R} {check_mid}")
            if check_mid:
                ans=mid
                R=mid-1
            else:
                L=mid+1
        return ans

        
        