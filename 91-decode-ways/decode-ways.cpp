class Solution {
public:
    int numDecodings(string s) {
        vector<int> cache(s.length() + 1, 0);
        cache[s.length()] = 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == '0') {
                cache[i] = 0;
                continue;
            }
            int count = 0;
            if (i != s.length() - 1 &&
                (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6')))
                count += cache[i + 2];
            count += cache[i + 1];
            cache[i] = count;
        }
        return cache[0];
    }
};