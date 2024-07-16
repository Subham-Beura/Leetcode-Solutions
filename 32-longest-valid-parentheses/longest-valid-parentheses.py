class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[] 
        count=0
        arr=[0]*(len(s))
        for i,c in enumerate(s):
            if c==')' and stack and  stack[-1][0]=='(':
                arr[stack[-1][1]]=1
                arr[i]=1
                stack.pop()
            else:
                stack.append((c,i))
        maxCount=0 
        for a in arr:
            if a==0:
                count=0
            else:
                count+=1
                maxCount=max(maxCount,count)
        return maxCount
        