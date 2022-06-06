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

## 最小值

```
/* Given a non-empty binary search tree, return the node
with minimum key value found in that tree. Note that the
entire tree does not need to be searched. */
struct node* minValueNode(struct node* node)
{
    struct node* current = node;

    /* loop down to find the leftmost leaf */
    while (current && current->left != NULL)
        current = current->left;

    return current;
}
```

## 删除

BST的删除需要考虑三种情况： 

- 删除的是叶子节点
- 删除的节点仅有单个子节点
- 删除的节点有两个子节点，需要用右子树的最小值来替代

```
/* Given a binary search tree and a key, this function
deletes the key and returns the new root */
struct node* deleteNode(struct node* root, int key)
{
    // base case
    if (root == NULL)
        return root;

    // If the key to be deleted is
    // smaller than the root's
    // key, then it lies in left subtree
    if (key < root->key)
        root->left = deleteNode(root->left, key);

    // If the key to be deleted is
    // greater than the root's
    // key, then it lies in right subtree
    else if (key > root->key)
        root->right = deleteNode(root->right, key);

    // if key is same as root's key, then This is the node
    // to be deleted
    else {
        // node has no child
        if (root->left==NULL and root->right==NULL)
            return NULL;

        // node with only one child or no child
        else if (root->left == NULL) {
            struct node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            struct node* temp = root->left;
            free(root);
            return temp;
        }

        // node with two children: Get the inorder successor
        // (smallest in the right subtree)
        struct node* temp = minValueNode(root->right);

        // Copy the inorder successor's content to this node
        root->key = temp->key;

        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}
```
