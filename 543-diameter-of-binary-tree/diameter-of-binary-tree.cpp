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
    int noOfNodesInDia=-1;
    int maxHeight(TreeNode* root){
        if(root==NULL)
            return 0;

        int leftHeight=maxHeight(root->left);
        int rightHeight=maxHeight(root->right);

        noOfNodesInDia=max(noOfNodesInDia,leftHeight+rightHeight+1);
        return max(leftHeight,rightHeight)+1;

    }
    int diameterOfBinaryTree(TreeNode* root) {
        maxHeight(root);
        return noOfNodesInDia-1;
    }
};