##

二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。


示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：

节点数量不会超过 100000。

```
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
    void travseBiTreeInOrder(TreeNode* root, TreeNode*& pre, TreeNode*& head) {
        if (root == nullptr) {
            return;
        }
        travseBiTreeInOrder(root->left, pre, head);

        // 递归遍历第一次返回的时候即找到了最左边的节点
        // 最左边的节点是需要返回的节点，因此保存起来
        if (pre == nullptr) {
            head = root;
        }

        // 如果pre不为空，即已经获得了前节点
        // 此时，执行节点的修改操作:
        // 1) 前节点的右支指向当前节点
        // 2）当前节点的左支赋值为空（变为单向链表）
        if (pre != nullptr) {
            pre->right = root;
        }
        root->left = nullptr;

        // 将当前节点保存下来，作为下一次访问节点的前节点
        pre = root;

        travseBiTreeInOrder(root->right, pre, head);
    }

    TreeNode* convertBiNode(TreeNode* root) {
        travseBiTreeInOrder(root, _pre, _head);
        return _head;
    }

    TreeNode* _pre{nullptr};
    TreeNode* _head{nullptr};
};
```
