class Solution:
    def checkIfPossibleToday(self,i,bloomDay,noOfB,k):
        consecutive_length, bouquets = 0, 0
        for bloom in bloomDay:
            if bloom <= i:
                consecutive_length += 1
                if consecutive_length >= k:
                    consecutive_length = 0
                    bouquets += 1
            else:
                consecutive_length = 0
        res=bouquets>=noOfB
        # print(res)
        return res

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m * k):
            return -1

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

        
        