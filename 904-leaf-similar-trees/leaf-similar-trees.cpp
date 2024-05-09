/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    vector<int> leaf1;
    vector<int> leaf2;
    void getLeafsLeftToRight(TreeNode* root) {
        if(root==NULL){
            return;
        }
        if (root->left == NULL && root->right == NULL) {
            leaf1.push_back(root->val);
            return;
        }
        getLeafsLeftToRight(root->left);
        getLeafsLeftToRight(root->right);
    }
    void getLeafsLeftToRight2(TreeNode* root) {
        if(root==NULL){
            return;
        }
        if (root->left == NULL && root->right == NULL) {
            leaf2.push_back(root->val);
            return;
        }
        getLeafsLeftToRight2(root->left);
        getLeafsLeftToRight2(root->right);
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        getLeafsLeftToRight(root1);
        getLeafsLeftToRight2(root2);
        if (leaf1.size() != leaf2.size()) {
            return false;
        }
        for (int i = 0; i < leaf1.size(); i++) {
            if (leaf1[i] != leaf2[i])
                return false;
        }
        return true;
    }
};