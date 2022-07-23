## 列处理/awk

将文本行划分为列进行处理。

```
cat cycle.txt | awk 'BEGIN {FS="="} $1 {print $2}' > ca-data # 对每行按照"="进行分列，并输出第2列。
```
