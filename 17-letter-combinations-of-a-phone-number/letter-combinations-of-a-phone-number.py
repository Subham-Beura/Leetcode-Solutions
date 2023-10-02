class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
          return []
        lToN={
          2:'abc',
          3:'def',
          4:'ghi',
          5:'jkl',
          6:'mno',
          7:'pqrs',
          8:'tuv',
          9:'wxyz',
        } 
        res=[]
        n=len(digits)
        def dfs(i,cur):
          if i==n:
            res.append(cur)
            return 
          if i>n:
            return 

          No=int(digits[i])
          letters=lToN[No]

          for c in letters:
            dfs(i+1,cur+c)
        dfs(0,'')
        return res

