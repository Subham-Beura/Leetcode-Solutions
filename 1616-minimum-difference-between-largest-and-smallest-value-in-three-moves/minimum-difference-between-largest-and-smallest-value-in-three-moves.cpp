class Solution {
public:
    int minDifference(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        if(nums.size()<=4)
            return 0;
        sort(nums.begin(),nums.end());
        int minDiff=INT_MAX;
        for(int i=0;i<4;i++){
            int L=i,R=nums.size()-1-(3-i);
            minDiff=min(minDiff,nums[R]-nums[L]);
        }
        return minDiff;
    }
};