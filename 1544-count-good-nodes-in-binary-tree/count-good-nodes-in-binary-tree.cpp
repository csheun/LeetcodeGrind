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
    int goodNodes(TreeNode* root) {
        int res{0};
        if (!root) return res;
        helper(root, root->val, res);
        return res;
    }
private:
    void helper(TreeNode* root, int max_seen, int& res) {
        if (!root) return;
        if (root->val >= max_seen) {
            res += 1;
        }
        max_seen = max(root->val, max_seen);
        helper(root->left, max_seen, res);
        helper(root->right, max_seen, res);
    }
};