class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> found;

        int L = 0, R = 0, n = s.size();
        int maxV = 0;
        while (L < n && R < n) {
            if (found.find(s[R]) != found.end()) {
                while (found.find(s[R]) != found.end()) {
                    found.erase(s[L]);
                    L++;
                }
            } else {
                maxV = max(R - L + 1, maxV);
            }
            found.insert(s[R]);
            R += 1;
        }
        return maxV;
    }
};