class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        cache={}
        def noSchemes(i,no,score):
            # print(str(i)+" "+str(no)+" "+str(score))
            if (i,no,score) in cache:
                return cache[(i,no,score)]
            if no<0:
                cache[(i,no,score)]=0
                return 0
            if i==len(group)-1:
                cache[(i,no,score)]= 1 if score>=minProfit else 0
                return cache[(i,no,score)]
            doJob,noJob=0,0
            if no-group[i+1]>=0:
                doJob=noSchemes(i+1,no-group[i+1],min(minProfit,score+profit[i+1]))
            noJob=noSchemes(i+1,no,score)

            cache[(i,no,score)]= doJob+noJob
            return cache[(i,no,score)]
        return (noSchemes(0,n,0)+noSchemes(0,n-group[0],profit[0]))%(10**9+7)