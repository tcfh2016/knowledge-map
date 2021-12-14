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

void inOrderBinaryTree(Node* root, vector<int> &ans)
{
    if (root == nullptr) {
        return ;
    }

    if (root->left != nullptr) {
        inOrderBinaryTree(root->left, ans);
    }
    ans.push_back(root->data);
    if (root->right != nullptr) {
        inOrderBinaryTree(root->right, ans);
    }
}

//Function to return a list containing the preorder traversal of the tree.
vector <int> inOrder(Node* root)
{
    if (root == nullptr) {
        return {};
    }

    vector<int> answer;
    inOrderBinaryTree(root, answer);
    return answer;
}
