## 翻转二叉树

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1


## 解法

1）二叉树的多数算法都和递归相关，二叉树的翻转如果从层次遍历上去考虑，那么就是“先左后右”变更为“先右后左”:

```
TreeNode* invertTree(TreeNode* root) {
    invertTreeR(root);
    return root;
}

void invertTreeR(TreeNode* root) {
    if (root == nullptr) {
        return ;
    }
    swap(root->left, root->right);
    if (root->left != nullptr) {
        invertTreeR(root->left);
    }
    if (root->right != nullptr) {
        invertTreeR(root->right);
    }
}
```

2）继续层次遍历，那么也是一样，需要交换左右子树

```
TreeNode* invertTree(TreeNode* root) {
if (root == nullptr) {
    return root;
}

queue<TreeNode*> q;
q.push(root);

while (not q.empty()) {
    auto e = q.front();
    q.pop();

    swap(e->left, e->right);
    if (e->left != nullptr) {
        q.push(e->left);
    }
    if (e->right != nullptr) {
        q.push(e->right);
    }
}

return root;
}
```
