class Solution {
public:
    int appendCharacters(string s, string t) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        int j = 0;
        for (char c : s) {
            if (c == t[j])
                j++;
        }
        return t.size() - j;
    }
};