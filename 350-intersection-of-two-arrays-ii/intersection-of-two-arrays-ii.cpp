class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();

        unordered_map<int, int> map;
        for(int i=0;i<n1;i++){
            map[nums1[i]]++;
        }

        vector<int> res;
        for(int a:nums2){
            if(!map[a])
                continue;
            map[a]--; 
            res.push_back(a);
        }

        return res;
    }
};