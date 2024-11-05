class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(s1, s2):
            n = len(s1)
            m = len(s2)

            dp = [[0] * (m + 1) for _ in range(n + 1)]
            for r in range(n - 1, -1, -1):
                for c in range(m - 1, -1, -1):
                    if s1[r] == s2[c]:
                        dp[r][c] = dp[r + 1][c + 1] + 1
                    else:
                        dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
            return dp[0][0]
        return len(word1)+len(word2)-2*(lcs(word1,word2))
