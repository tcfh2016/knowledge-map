#include <iostream>
#include <stack>
#include <queue>

template <typename T>
struct BinTreeNode {
  T data;
  BinTreeNode *leftNode;
  BinTreeNode *rightNode;
  BinTreeNode *parent;
};

// 先序遍历: 递归
template <typename T>
void preorderTraversal_R(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  std::cout <<root->data <<std::endl;
  preorderTraversal(root->leftNode);
  preorderTraversal(root->rightNode);
}

template <typename T>
void preorderTraversal(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  std::stack<T> s;
  s.push(root);
  while (!s.empty()) {
    root = s.pop();
    std::cout <<root->data <<std::endl;
    if (root->rightNode != nullptr) {
      s.push(root->rightNode);
    }
    if (root->leftNode != nullptr) {
      s.push(root->leftNode);
    }
  }
}

// 中序遍历，递归实现
template <typename T>
void inorderTraversal_R(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  inorderTraversal(root->leftNode);
  std::cout <<root->data <<std::endl;
  inorderTraversal(root->rightNode);
}

template <typename T>
void inorderTraversal(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  std::stack<T> s;
  while (root != nullptr or not s.empty()) {
    // 将当前节点所有左节点全部入栈
    while (root != nullptr) {
      s.push(root);
      root = root->leftNode;
    }

    // 栈不为空
    while (not s.empty()) {
      auto node = s.pop();
      std::cout <<node->data <<std::endl;
      root = node.right;
    }
  }
}

// 后序遍历，递归
template <typename T>
void postorderTraversal_R(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  postorderTraversal_R(root->leftNode);
  postorderTraversal_R(root->rightNode);
  std::cout <<root->data <<std::endl;
}

template <typename T>
void postorderTraversal(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  //TODO
}

// 层次遍历，递归
template <typename T>
void levelTraversal(BinTreeNode<T> *root) {
  if (root == nullptr) {
    return;
  }
  std::queue<T> q;
  q.push(root);

  while (not q.empty()){
    auto x = q.pop();
    std::cout <<x->data <<std::endl;
    if (x->leftNode != nullptr) {
      q.push(x->leftNode);
    }
    if (x->rightNode != nullptr) {
      q.push(x->rightNode);
    }
  }
}
