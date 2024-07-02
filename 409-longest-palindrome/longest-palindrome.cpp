class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> map;
        for (char c : s)
            map[c]++;
        int sum = 0;
        int maxOdd = 0;
        for (auto it = map.begin(); it != map.end(); it++) {
            if ((it->second & 1) == 0) {
                sum += it->second;
                continue;
            }
            sum += it->second - 1;
            maxOdd = 1;
            continue;
        }
        return (maxOdd) ? sum + 1 : sum;
    }
};