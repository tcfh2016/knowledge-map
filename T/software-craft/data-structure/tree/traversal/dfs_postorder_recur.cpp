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

void postOrderBinaryTree(Node* root, vector<int> &ans)
{
    if (root == nullptr) {
        return ;
    }

    if (root->left != nullptr) {
        postOrderBinaryTree(root->left, ans);
    }
    if (root->right != nullptr) {
        postOrderBinaryTree(root->right, ans);
    }
    ans.push_back(root->data);
}

//Function to return a list containing the preorder traversal of the tree.
vector <int> postOrder(Node* root)
{
    if (root == nullptr) {
        return {};
    }

    vector<int> answer;
    postOrderBinaryTree(root, answer);
    return answer;
}
