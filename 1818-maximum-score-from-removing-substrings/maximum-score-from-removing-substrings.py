class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        resv=s
        s=list(s)
        stack=[]
        highP='ab' if x>y else 'ba'
        lowP='ba' if x>y else 'ab'
        x,y=max(x,y),min(x,y)
        res=0
        for i,c in enumerate(s):
            # print(c)
            # print(stack)
            if c== highP[1] and stack and stack[-1]==highP[0]:
                # print("---")
                stack.pop()
                # print(stack)
                res+=x
                continue
            stack.append(c)
        s=stack
        stack=[]

        for i,c in enumerate(s):
            # print(c)
            # print(stack)
            if stack and c== lowP[1] and stack[-1]==lowP[0]:
                stack.pop()
                # print("---")
                # print(stack)
                res+=y
                continue
            stack.append(c)
        # print(y)
        # print(stack)
        return res
            