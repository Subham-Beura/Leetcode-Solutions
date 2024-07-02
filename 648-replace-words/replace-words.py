class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        sentence=sentence.split(" ")
        res=""
        # print(sentence)
        for i,word in enumerate(sentence):
            for root in dictionary:
                if root in word[:len(root)]:
                    sentence[i]=root
                    break
            res+=sentence[i]+" "
        return res[:-1]
        