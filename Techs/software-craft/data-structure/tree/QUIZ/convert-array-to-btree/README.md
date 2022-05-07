## 将有序数组转换为二叉搜索树

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 解法

第一次没有做过会觉得生疏，不过看过提示之后也能够慢慢摸索出使用递归的方式。新手容易犯错误是在针对起始和结束索引的操作上。

```
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return ConstructBST(nums, 0, nums.size() - 1);
    }

    TreeNode* ConstructBST(vector<int>& nums, int begin, int end) {
        if (begin > end) {
            return nullptr;
        }

        auto mid = (end + begin) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = ConstructBST(nums, begin, mid - 1);
        root->right = ConstructBST(nums, mid + 1, end);
        return root;
    }

};
```
