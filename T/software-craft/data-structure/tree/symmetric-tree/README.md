## 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


## 解法

刚开始一看拿不准思路，后面看了提示才觉得可以使用递归进行判断。

```
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) {
            return false;
        }
        return recur_symmetric_check(root->left, root->right);
    }

    bool recur_symmetric_check(TreeNode* l, TreeNode* r) {
        if (l == nullptr and r == nullptr) {
            return true;
        }

        if (l == nullptr or r == nullptr or l->val != r->val) {
            return false;
        }

        return recur_symmetric_check(l->right, r->left) and recur_symmetric_check(l->left, r->right);
    }
};
```
