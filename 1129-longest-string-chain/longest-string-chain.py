class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len) 

        n=len(words)
        cache={}

        # print(words)
        
        max_len=1
        for word in words:
            word_length=len(word)
            cache[word]=1
            for i in range(word_length):
                prev_word= word[:i]+word[i+1:] 
                if prev_word in words:
                    cache[word]=max(cache[word],cache[prev_word]+1)
            max_len=max(max_len,cache[word]) 
        # print(cache)
                
        return max_len 