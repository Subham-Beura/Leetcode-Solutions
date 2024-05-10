class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        int res = 1;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) 
                if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) 
                    dp[i] = dp[j] + 1;
            res = max(dp[i], res);
        }
        return res;
    }
};