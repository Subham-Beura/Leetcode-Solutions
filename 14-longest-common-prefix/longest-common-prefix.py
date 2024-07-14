class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=[len(s) for s in strs]
        for i in range(min(length)):
            first=strs[0][i]
            for s in strs:
                if s[i]!=first:
                    return strs[0][:i]
        return strs[0][:min(length)]
                