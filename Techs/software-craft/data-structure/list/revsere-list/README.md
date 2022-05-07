## 反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


## 解法

1）直观的迭代法，遍历然后进行前置插入即可。

```
ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
        return nullptr;
    }

    ListNode* new_head = new ListNode();
    while (head != nullptr) {
        auto t = head;
        head = head->next;

        t->next = new_head->next;
        new_head->next = t;            
    }
    return new_head->next;
}
```
