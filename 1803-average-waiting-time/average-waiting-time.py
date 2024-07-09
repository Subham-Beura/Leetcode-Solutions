class Solution:
    def averageWaitingTime(self, customer: List[List[int]]) -> float:
        n=len(customer)
        currentTime=customer[0][0]
        busyTill=currentTime+customer[0][1]
        total=customer[0][1]
        for i in range(1,n):
            entryTime=customer[i][0]
            timeTaken=customer[i][1]

            if entryTime>busyTill:
                busyTill=entryTime+timeTaken
                total+=timeTaken
            else:
                busyTill+=timeTaken
                total+=busyTill-entryTime
        return total/n