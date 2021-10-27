## 最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

## 解法

1）感觉就是用数组来模拟一个栈，然后用一个变量来保存最小元素。但是这样当pop出了最小元素就没有办法了。只能初略地用遍历来找最小值：

```
class MinStack {
public:
    MinStack() {

    }

    void push(int val) {
        elems.push_back(val);
    }

    void pop() {
        if (elems.size() != 0) {
            elems.pop_back();
        }
    }

    int top() {
        return elems.back();
    }

    int getMin() {        
        int t = elems[0];
        for (auto i = 1; i < elems.size(); ++i) {
            if (t > elems[i]) {
                t = elems[i];
            }
        }
        return t;
    }

    vector<int> elems;    
};
```

2）看了下提示是需要使用辅助栈来保存最小值

```
class MinStack {
public:
    MinStack() {

    }

    void push(int val) {
        elems.push(val);
        if (min_elems.empty() || val <= min_elems.top()) {
            min_elems.push(val);
        }
    }

    void pop() {
        if (elems.top() == min_elems.top()) {
            min_elems.pop();
        }
        elems.pop();
    }

    int top() {
        return elems.top();
    }

    int getMin() {    
        return min_elems.top();
    }

    stack<int> elems;
    stack<int> min_elems;  
};
```
