/*
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/

void preOrderBinaryTree(Node* root, vector<int> &ans)
{
    if (root == nullptr) {
        return ;
    }

    ans.push_back(root->data);
    if (root->left != nullptr) {
        preOrderBinaryTree(root->left, ans);
    }
    if (root->right != nullptr) {
        preOrderBinaryTree(root->right, ans);
    }
}

//Function to return a list containing the preorder traversal of the tree.
vector <int> preOrder(Node* root)
{
    if (root == nullptr) {
        return {};
    }

    vector<int> answer;
    preOrderBinaryTree(root, answer);
    return answer;
}
