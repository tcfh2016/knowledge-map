## std::next/ std::advance

Std::next and std::advance have same purpose which can be used to advance the iterator by a certain position:

```
template
void advance( InputIt& it, Distance n );

ForwardIterator next (ForwardIterator it,
       typename iterator_traits::difference_type n = 1);
```

The differences includes:

- std::next will advance by one by default, whereas std::advance() requires a distance.
- std::next returns an iterator after advancing n positions from the given base position, whereas std::advance does not return anything.
- std::next returns a new iterator to the desired position, whereas std::advance modifies its argument pointing to the desired position.


参考：

- [std::next vs std::advance in C++](https://www.geeksforgeeks.org/stdnext-vs-stdadvance-in-cpp/)
- [What's the difference between std::advance and std::next?](https://stackoverflow.com/questions/15017065/whats-the-difference-between-stdadvance-and-stdnext)
