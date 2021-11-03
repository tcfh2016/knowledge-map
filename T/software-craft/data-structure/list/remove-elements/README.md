##  移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

## 解法

这个很简单呀，就是逐个遍历，主要是要用前后两个指针一起走。不过调试的时候还是犯了两个错误：一个是误把“==”写为“=”，还有就是疏忽的判空处理，考虑了一层没有考虑第二层。

```
ListNode* removeElements(ListNode* head, int val) {
        while ( head != nullptr and head->val == val) {
            auto t = head;
            head = head->next;
            delete t;
        }
        if (head == nullptr) {
            return nullptr;
        }

        auto pre = head;
        auto cur = head->next;
        while (cur != nullptr) {
            if (cur->val == val) {
                pre->next = cur->next;
                delete cur;
                cur = pre->next;
            }
            else {
                pre = pre->next;
                cur = cur->next;
            }
        }
        return head;
    }
```
