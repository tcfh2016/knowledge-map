## 按照某列的数据进行拆分

需求：按照某列的值进行区分。并且分拆到不同的DataFrame里面？

## 第一个问题：怎么知道某列有哪些值？

可以使用`unique()`函数，如`dataframe["column"].unique()`。然后，我们就可以通过条件选择来过滤，从而将一个DataFrame拆分为多个DataFrame。

参考：

- [What is the unique function in pandas?](https://www.educative.io/answers/what-is-the-unique-function-in-pandas)


## 第二个问题：怎样按照值的范围进行拆分？

参考：

- [](https://stackoverflow.com/questions/21441259/pandas-groupby-range-of-values)
