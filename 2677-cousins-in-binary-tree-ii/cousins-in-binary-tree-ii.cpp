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
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (root == nullptr) return root;
        TreeNode* res = root;
        int id{0};
        queue<pair<int, TreeNode*>> q;
        q.push({id, root});
        queue<pair<int, TreeNode*>> q1;
        while(! q.empty()) {
            // Add up all in q.
            int sum{0};
            unordered_map<int, int> id_sum_map;
            queue<pair<int, TreeNode*>> tmp = q;
            while (! tmp.empty()) {
                pair<int, TreeNode*> curr = tmp.front();
                tmp.pop();
                id_sum_map[curr.first] += curr.second->val;
                sum += curr.second->val;
            }
            id = 0;
            while (! q.empty()) {
                pair<int, TreeNode*> curr = q.front();
                q.pop();
                int new_val = sum - id_sum_map[curr.first];
                TreeNode* node = curr.second;
                node->val = new_val;
                if (node->left != nullptr) q1.push({id, node->left});
                if (node->right != nullptr) q1.push({id, node->right});
                id++;
            }
            q = q1;
            q1 = queue<pair<int, TreeNode*>>();
        }
        return res;
    }
};