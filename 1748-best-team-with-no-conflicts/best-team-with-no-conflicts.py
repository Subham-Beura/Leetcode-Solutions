class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        ageAndScore=list(zip(ages,scores))
        ageAndScore.sort(key=lambda x:(x[0],x[1]))
        dp=[0]*len(scores)
        ans=0
        for i,(age,score) in enumerate(ageAndScore):
            dp[i]=score
            for j in range(i):
                yPlayer=ageAndScore[j]
                if yPlayer[1]<=score and dp[j]+score>dp[i]:
                    dp[i]=dp[j]+score
                
            if dp[i]>ans:
                ans=dp[i]
        return ans  

        # ageAndScore=list(zip(ages,scores))
        # ageAndScore.sort(key=lambda x:x[0])
        # cache={}
        # def maxScore(ageAndScore):
        #     tageAndScore=tuple(ageAndScore)
            
        #     if tageAndScore in cache:
        #         return cache[tageAndScore]
            
        #     if ageAndScore==[]:
        #         return 0
        #     player=ageAndScore[0]
        #     age=player[0]
        #     score=player[1]

        #     dontTake=maxScore(ageAndScore[1:])

        #     newAgeAndScore=filter(lambda x: not (x[0]>age and x[1]<score) ,ageAndScore)
        #     take=maxScore(newAgeAndScore[1:])+score
            
        #     cache[tageAndScore]= max(dontTake,take)
        #     return cache[tageAndScore]
        # res= maxScore(ageAndScore)
        # print(cache)
        # return res