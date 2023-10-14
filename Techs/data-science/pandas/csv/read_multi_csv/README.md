## 读取多个csv文件

逐个读取在进行合并：

```
dfs = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(dfs, ignore_index=True)
print(concatenated_df)
```


参考：

- [Import multiple CSV files into pandas and concatenate into one DataFrame](https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe)
- [Pandas Read Multiple CSV Files into DataFrame](https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/)