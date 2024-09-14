## bitset

如果用来管理固定大小的bit位或者boolean值，可以使用`bitset`。对于变长的需求，那么就需要使用`vector<bool>`。

C++11增加了与string交互的特性，比如可以直接将bitset转换为字符串，也可以通过字符串来初始化bitset：

```
string s = bitset<80>(12345678).to_string(); // C++11
string s = bitset<80>(12345678).to_string<char, char_traits<char>, allocator<char> >(); // before C++11

bitset<100>("1000101011"); // C++11
bitset<100>(string("1000101011")); // before C++11
```
