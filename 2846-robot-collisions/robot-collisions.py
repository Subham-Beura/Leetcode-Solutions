class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots=[[0]*4 for _ in range(len(positions))]
        for i in range(len(positions)):
            robots[i][0]=positions[i]
            robots[i][1]=healths[i]
            robots[i][2]=1 if directions[i]=='R' else -1
            robots[i][3]=i

        robots.sort(key= lambda x: x[0])  
        # print(robots)
        stack=[robots[0]]
        for i in range(1,len(robots)):
            newR=robots[i]
            # print(f"-----{newR}----")
            # print(stack)
            while stack and newR[2]<0 and stack[-1][2]>0 and newR[1]>0:
                # print(newR)
                # print(stack)
                wDiff=newR[1]-stack[-1][1]
                if wDiff>0:
                    # NewR survives
                    healths[stack[-1][3]]=0
                    newR[1]=max(0,newR[1]-1)
                    healths[newR[3]]=newR[1]
                    stack.pop()
                elif wDiff==0:
                    stack[-1][1]=0
                    healths[stack[-1][3]]=0
                    newR[1]=0
                    healths[newR[3]]=0
                    stack.pop()
                else:
                    # OldOneSurvives
                    stack[-1][1]=max(0,stack[-1][1]-1)
                    healths[stack[-1][3]]=stack[-1][1]
                    newR[1]=0
                    healths[newR[3]]=0
            if newR[1]>0:
                stack.append(newR)
            
        # print(stack)
        # print(robots) 
        # print(healths)
        # res=[i[1] for _ in robots]
        # return res
        res=[]
        for h in healths:
            if h>0:
                res.append(h)
        return res