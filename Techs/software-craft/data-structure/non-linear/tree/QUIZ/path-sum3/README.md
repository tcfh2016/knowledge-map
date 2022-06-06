## 路径总和 III

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

## 解法

最明显是用递归，不过每次递归的写法都感觉有些模糊，而这里可能还需要双层递归。一层用来计算路径和，一层用来遍历二叉树的各个节点。比如下面的实现第二层递归就是先序遍历的实现。


```
int countPathSum(TreeNode *root, int targetSum) {
       if (root == nullptr) {
           return 0;
       }

       auto l = countPathSum(root->left, targetSum - root->val);
       auto r = countPathSum(root->right, targetSum - root->val);
       return l + r + (root->val == targetSum ? 1 : 0);
   }

 int pathSum(TreeNode* root, int targetSum) {
     if (root == nullptr) {
         return 0;
     }

     auto cur = countPathSum(root, targetSum);
     auto l = pathSum(root->left, targetSum);
     auto r = pathSum(root->right, targetSum);

     return cur + l + r;
 }
```
