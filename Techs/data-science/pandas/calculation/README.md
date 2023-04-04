
## 求与前一行的差值

```
df['output']=df['input'] -df['input'].shift(1)
```

参考：

- [](https://stackoverflow.com/questions/57801048/subtract-previous-row-value-from-the-current-row-value-in-a-pandas-column)