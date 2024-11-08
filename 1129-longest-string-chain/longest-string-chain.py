class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: (len(x),x)) 

        n=len(words)
        cache=[1]*n

        def isChain(smaller,bigger):
            if smaller in bigger:
                return True
            for i,c in enumerate(bigger):
                if bigger[:i]+bigger[i+1:] ==smaller:
                    return True 
            return False
        # print(words)
        max_len=1
        for i in range(n-2,-1,-1):
            word_length=len(words[i])
            for j in range(i+1,n):
                if len(words[j])>word_length+1:
                    break
                if len(words[j])==word_length or not isChain(words[i],words[j]):
                    continue
                # print(f"{words[i]} : {words[j]}")
                cache[i]=max(cache[i],cache[j]+1)
            max_len=max(max_len,cache[i]) 
        print(cache)
                
        return max_len 