## 相交链表

编写一个程序，找到两个单链表相交的起始节点。

## 解法

1）最直白的方法就是两个循环，逐个去查找，但是这样子遍历比较费劲，因为链表不支持随机访问，每次定位到初始节点比较费力。要么就是用set/hashtable来存放其中一个链表的节点，然后遍历第二个链表来查找：

```
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    set<ListNode *> A;
    ListNode *ha = headA;
    while (ha != nullptr) {
        A.insert(ha);
        ha = ha->next;
    }

    ListNode *hb = headB;
    while (hb != nullptr && A.size() > 0) {
        if (A.count(hb) > 0) {
            return hb;
        }
        hb = hb->next;
    }
    return nullptr;
}
```

2）另外一种方法就是比较巧妙的用双指针进行遍历，且计算路径
