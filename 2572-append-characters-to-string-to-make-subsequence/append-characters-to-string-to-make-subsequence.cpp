class Solution {
public:
    int appendCharacters(string s, string t) {
        int  j = 0;
        // while (i < s.size() && j < t.size() && s[i] == t[j]) {
        //     i++;
        //     j++;
        // }
        for (auto c:s) {
            if (c == t[j])
                j++;
        }
        return t.size() - j;
    }
};