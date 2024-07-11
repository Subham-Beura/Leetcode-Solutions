class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for c in s:
            if c !=')':
                stack.append(c)
                continue
            i=len(stack)-1
            q=[]
            while stack and i>=0 and stack[i]!='(':
                k=stack.pop()
                q.append(k)  
                i-=1
            stack.pop()
            stack.extend(q)
            # print(stack)
        return ''.join(str(e) for e in stack)