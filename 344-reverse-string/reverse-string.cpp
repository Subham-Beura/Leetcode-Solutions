class Solution {
public:
    void reverseString(vector<char>& s) {
        int L=0;
        int R=s.size()-1;
        while(L<R)
            swap(s[L++],s[R--]);
        
    }
};