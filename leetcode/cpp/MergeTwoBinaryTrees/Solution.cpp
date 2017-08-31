/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL && t2 != NULL) {
            t1 = new TreeNode(0);
        }
        if (t1 != NULL && t2 != NULL) {
            // merge value
            t1->val += t2->val;
            // merge left node
            t1->left = mergeTrees(t1->left, t2->left);
            // merge right node
            t1->right = mergeTrees(t1->right, t2->right);
        }
        return t1;
    }
};