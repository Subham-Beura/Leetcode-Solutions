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
    int maxPath;
    int maxPathFromRootToLeaf(TreeNode* root){
        if(root==NULL)
            return 0;

        int leftVal=max(0,maxPathFromRootToLeaf(root->left));
        int rightVal=max(0, maxPathFromRootToLeaf(root->right));
        maxPath=max({maxPath,leftVal+rightVal+root->val});

        return root->val+max(leftVal,rightVal);
    }
    int maxPathSum(TreeNode* root) {
        maxPath=root->val;
        maxPathFromRootToLeaf(root);
        return (maxPath);
    }
};