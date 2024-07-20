 class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum,
                                      vector<int>& colSum) {

        vector<vector<int>> res(rowSum.size(),vector<int>(colSum.size(),0));
        for( int r=0;r<rowSum.size();r++)
            for(int c=0;c<colSum.size();c++){
                res[r][c]=min(rowSum[r],colSum[c]);
                rowSum[r]-=res[r][c];
                colSum[c]-=res[r][c];
            }
        return res;
    }
};