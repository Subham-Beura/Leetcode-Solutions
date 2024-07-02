class Solution {
public:
    bool dfs(vector<vector<char>>& G, int r, int c) {
        int R = G.size();
        int C = G[0].size();
        if (r < 0 or c < 0 or r >= R or c >= C)
            return false;
        if (G[r][c] == '0')
            return false;
        G[r][c] = '0';
        dfs(G, r + 1, c);
        dfs(G, r - 1, c);
        dfs(G, r, c + 1);
        dfs(G, r, c - 1);
        return true;
    }
    int numIslands(vector<vector<char>>& G) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        int R = G.size();
        int C = G[0].size();
        int res = 0;
        for (int r = 0; r < R; r++)
            for (int c = 0; c < C; c++) {
                if (G[r][c] == '1') {
                    dfs(G, r, c);
                    res++;
                }
            }
        return res;
    }
};