class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> map;
        for (char c : s)
            map[c]++;
        int sum = 0;
        bool maxOdd = false;
        for (auto it = map.begin(); it != map.end(); it++) {
            if ((it->second & 1) == 0) {
                sum += it->second;
                continue;
            }
            sum += it->second - 1;
            maxOdd = true;
            continue;
        }
        return maxOdd ? sum + 1 : sum;
    }
};