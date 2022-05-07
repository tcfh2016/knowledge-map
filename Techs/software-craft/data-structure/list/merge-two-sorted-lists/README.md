## 合并有序链表

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


## 解法

1）直观的解法

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        }
        if (l2 == nullptr) {
            return l1;
        }

        ListNode* head = nullptr;
        ListNode* curr = nullptr;
        if (l1->val < l2->val) {
            head = curr = l1;
            l1 = l1->next;
        }
        else {
            head = curr = l2;
            l2 = l2->next;
        }

        while (l1 != nullptr and l2 != nullptr) {
            if (l1->val < l2->val) {
                curr->next = l1;
                curr = l1;
                l1 = l1->next;
            }
            else {
                curr->next = l2;
                curr = l2;
                l2 = l2->next;
            }
        }
        if (l1 != nullptr) {
            curr->next = l1;
        }
        if (l2 != nullptr) {
            curr->next = l2;
        }

        return head;
    }
};
```

2）优化后的版本

```
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      ListNode head;
      ListNode* tail = &head;

      while (l1 != nullptr && l2 != nullptr) {
        if (l1->val < l2->val) {
          tail->next = l1;
          l1 = l1->next;
        }
        else {
          tail->next = l2;
          l2 = l2->next;
        }
        tail = tail->next;
      }
      tail->next = l1 == nullptr ? l2 : l1;
      return head.next;
    }
};
```

3）递归的方案

```
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      if (l1 == nullptr) {
        return l2;
      }
      if (l2 == nullptr) {
        return l1;
      }

      if (l1->val < l2->val) {
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
      }
      else {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
      }      
    }      
};
```
