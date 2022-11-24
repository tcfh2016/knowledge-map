## 列处理/awk

将文本行划分为列进行处理。

```
cat cycle.txt | awk 'BEGIN {FS="="} $1 {print $2}' > ca-data # 对每行按照"="进行分列，并输出第2列。
```



2017年10月17日16:55:19
今天编写一个统计代码量的小工具，将每次提交的修改信息录入到csv文件。下一步计划：

- 支持一步到位，不需要预先准备输入数据；
- 支持指定时间区域。

```
#!/bin/bash

function ParseStatisticsLine
{
  echo -n "$commitId," >> test.stat

  changedFileNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $1}'`)
  echo -n "$changedFileNum," >> test.stat

  insertedLineNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $2}'`)
  echo -n "$insertedLineNum," >> test.stat

  deletedLineNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $3}'`)
  echo "$deletedLineNum" >> test.stat

  # 注1：在赋值时使用“()”有特殊意义，将会截取
  # 注2：语法上规定变量在赋值时“=”左右两边不能有空格。
}

echo "SHA1,ChangedFiles,InsertedLines,DeletedLines" > $1.stat

for commitId in `cat $1`
do
  echo $commitId

  statisticsLine=`git show --stat $commitId | grep -i "changed,"`
  ParseStatisticsLine
done

cp $1.stat $1.csv

```
