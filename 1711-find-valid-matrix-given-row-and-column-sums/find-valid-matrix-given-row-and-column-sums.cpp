class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum,
                                      vector<int>& colSum) {

        vector<vector<int>> res(rowSum.size(), vector<int>(colSum.size(), 0));
        for (int r = 0; r < rowSum.size(); r++) {
            for (int c = 0; c < colSum.size(); c++) {
                if(colSum[c]==0)
                    continue;
                res[r][c] = min(rowSum[r], colSum[c]);
                rowSum[r] -= res[r][c];
                colSum[c] -= res[r][c];
                if (rowSum[r] == 0)
                    break;
            }
        }
        return res;
    }
};