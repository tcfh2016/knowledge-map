## Binary Search Tree （二叉搜索树）

二叉搜索树的定义：

- 某个节点左子树上所有节点小于该节点（左子树也是BST）
- 某个节点右子树上所有节点大于该节点（右子树也是BST）
- 没有重复节点

二叉树的如上特征让元素的搜索，最小值和最大值的获取变得更加便捷。

## 搜索

类似有序数组的二分搜索，先找到中点的元素，然后逐步缩小搜索范围。在二叉搜索树里面则从root元素开始，再逐步走向左子树或者右子树进行搜索。

```

// C function to search a given key in a given BST
struct node* search(struct node* root, int key)
{
    // Base Cases: root is null or key is present at root
    if (root == NULL || root->key == key)
       return root;

    // Key is greater than root's key
    if (root->key < key)
       return search(root->right, key);

    // Key is smaller than root's key
    return search(root->left, key);
}
```


## 插入

```
// Insert function definition.
BST* BST ::Insert(BST* root, int value)
{
    if (!root)
    {
        // Insert the first node, if root is NULL.
        return new BST(value);
    }

    // Insert data.
    if (value > root->data)
    {
        // Insert right node data, if the 'value'
        // to be inserted is greater than 'root' node data.

        // Process right nodes.
        root->right = Insert(root->right, value);
    }
    else
    {
        // Insert left node data, if the 'value'
        // to be inserted is greater than 'root' node data.

        // Process left nodes.
        root->left = Insert(root->left, value);
    }

    // Return 'root' node, after insertion.
    return root;
}
```

上面的算法，比我自己写的要美很多：

```
void searchBST(Node *root, int key) {
    if (root == nullptr or root->data == key) {
        return;
    }

    if (root->data > key) {
        if (root->left != nullptr) {
            return searchBST(root->left, key);    
        }
        else {
            Node *new_node = new Node(key);
            root->left = new_node;
        }
    }
    else {
        if (root->right != nullptr) {
            return searchBST(root->right, key);    
        }
        else {
            Node *new_node = new Node(key);
            root->right = new_node;
        }
    }
}

// Function to insert a node in a BST.
Node* insert(Node* root, int Key) {
    if (root != nullptr) {
        searchBST(root, Key);
    }

    return root;
}
```
