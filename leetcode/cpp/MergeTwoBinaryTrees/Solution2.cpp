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
        if (!t1) {
            return t2;
        }

        // initial first node pair
        pair<TreeNode*, TreeNode*> tmpPair(t1, t2);
        stack<pair<TreeNode*, TreeNode*> > tmpStack;
        tmpStack.push(tmpPair);

        while (tmpStack.size() != 0) {
            pair<TreeNode*, TreeNode*> tmpPair = tmpStack.top();
            tmpStack.pop();
            // n1 won't be NULL
            TreeNode* n1 = tmpPair.first;
            TreeNode* n2 = tmpPair.second;
            if (!n2) {
                continue;
            }
            n1->val += n2->val;
            if (!n1->left) {
                n1->left = n2->left;
            } else {
                tmpStack.push(make_pair(n1->left, n2->left));
            }
            if (!n1->right) {
                n1->right = n2->right;
            } else {
                tmpStack.push(make_pair(n1->right, n2->right));
            }
        }

        return t1;
    }
};