## 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

## 解法

直觉上是用递归，大致思路是判断根节点是否为空：

- 为空：深度为0，返回
- 不为空：返回 1 + max(左子树，右子树)

```
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        else{
            return calcMaxDepth(root);
        }
    }

    int calcMaxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return max(calcMaxDepth(root->left), calcMaxDepth(root->right)) + 1;
    }
};
```

另外一种方式是进行树的层次遍历。层次遍历的算法里面会使用队列进行辅助，但是在题目里面我们如何才能够记录每一层是否已经遍历完？

一种方法是记录每层的个数，然后每次遍历一层的时候将其从队列里面删除。

```
int maxDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }
    int depth = 0;
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        ++depth;
        auto size = q.size();
        for (auto i = 0; i < size; ++i) {
            auto f = q.front();
            if (f->left != nullptr) {
                q.push(f->left);
            }
            if (f->right != nullptr) {
                q.push(f->right);
            }
            q.pop();
        }
    }
    return depth;
}
```
