class Solution {
public:
    int appendCharacters(string s, string t) {
        int j = 0;
        for (char c : s) {
            if (c == t[j])
                j++;
        }
        return t.size() - j;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();