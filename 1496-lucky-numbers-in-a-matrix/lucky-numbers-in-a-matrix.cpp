class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        vector<int> minInRow(matrix.size(),INT_MAX),maxInCol(matrix[0].size(),INT_MIN);
        for(int r=0;r<matrix.size();r++){
            for (int c=0;c<matrix[0].size();c++){
                minInRow[r]=min(minInRow[r],matrix[r][c]);
                maxInCol[c]=max(maxInCol[c],matrix[r][c]);
            }
        }
        vector<int> res;
        for(int r=0;r<matrix.size();r++)
            for (int c=0;c<matrix[0].size();c++)
                if (matrix[r][c]==minInRow[r] && matrix[r][c]==maxInCol[c])
                    res.push_back(matrix[r][c]);
        return res;
    }
};