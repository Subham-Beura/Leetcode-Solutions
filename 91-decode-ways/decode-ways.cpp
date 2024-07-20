class Solution {
public:
    int findNumber(string s, int i, int n) {
        if (i == n) {
            return 1;
        }
        if (s[i] == '0') {
            return 0;
        }
        int count = 0;
        if (i != n - 1 && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
            count += findNumber(s, i + 2, n);
        }
        count += findNumber(s, i + 1, n);
        return count;
    }
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