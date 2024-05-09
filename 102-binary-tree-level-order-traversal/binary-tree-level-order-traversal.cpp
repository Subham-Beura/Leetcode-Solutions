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
    vector<vector<int>> levels;
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL)
            return {};
        vector<TreeNode*> currLevel;
        vector<TreeNode*> nextLevel;
        currLevel.push_back(root);

        vector<int> nodeValueCurrLevel;
        while (currLevel.size() != 0) {
            nodeValueCurrLevel={};
            for (TreeNode* n : currLevel) {
                nodeValueCurrLevel.push_back(n->val);
                if (n->left)
                    nextLevel.push_back(n->left);
                if (n->right)
                    nextLevel.push_back(n->right);
            }
            levels.push_back(nodeValueCurrLevel);
            currLevel = nextLevel;
            nextLevel = {};
        }
        return levels;
    }
};