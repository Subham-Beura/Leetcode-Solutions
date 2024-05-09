/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    void flipTree(TreeNode* root) {
        if(root==NULL)
            return;
        TreeNode* t=root->right;
        root->right=root->left;
        root->left=t;

        flipTree(root->left);
        flipTree(root->right);
    }
    TreeNode* invertTree(TreeNode* root) {
       flipTree(root) ;
       return root;
    }
};