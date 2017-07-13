
### sed 的基本用法

下面是一个使用sed来解析日志并将结果存储为csv格式的例子。

```

#!/bin/bash
function ParseCounter
{
	echo -n "$startTime," >> $OutputFile
  # 写入第一列数据，即每个文件中的时间戳。“-n”选项这里的意思是取消末尾的换行符，使内容输出到同一行。

	for((i=0;i<=11;i++));do
		PMID="M8061C$i"
		counter=(`cat $InputFile | sed "s/^.*<${PMID}>//g" | sed "s/<\/${PMID}>.*//g"`)
		echo -n "$counter," >> $OutputFile
    # 找到对应的数据，将其写入输出文件中，遵从csv格式。
	done
	PMID="M8061C19"
	counter=(`cat $InputFile | sed "s/^.*<${PMID}>//g" | sed "s/<\/${PMID}>.*//g"`)
	echo "$counter" >> $OutputFile
  # 找到其他数据，同样写入输出文件中。
}

# 清理现场，移除之前的统计。
rm LNCEL-*.stat LNCEL-*.csv

# 使用csv格式，提前准备好第一行的数据。再用excel工具打开csv格式时它们分别对应不同的列。
echo "startTime,M8061C0,M8061C1,M8061C2,M8061C3,M8061C4,M8061C5,M8061C6,M8061C7,M8061C8,M8061C9,M8061C10,M8061C11,M8061C19" > LNCEL-1.stat

# 当前需要针对三个cell进行分析，因此拷贝两次，准备好三个文件。
cp LNCEL-1.stat LNCEL-2.stat
cp LNCEL-1.stat LNCEL-3.stat

# 遍历指定的文件夹中的文件。
for file in `ls $1`
do
	if [ -d $1"/"$file ]   # 判断文件是否为文件夹。
	then    
		echo "is directory." # 不支持子文件夹的操作，碰到子文件夹则打印提示。
	else
		startTime=`cat $1"/"$file | sed 's/^.*startTime=//g' | sed 's/interval.*//g' | head -n 1 | sed 's/"//g'`
		echo $startTime
    # 通过sed的替换操作进行匹配行的解析，过程如下：
    # 1. 替换掉从“行首” 到 “*startTime=” 的字符，替换目标字符未指定，相当于删除操作。
    # 2. 替换掉从“interval.*” 到 “行尾” 的字符，替换目标字符未指定，相当于删除操作。
    #   （注：不能写成"interval*"，因为这里不是Windows下的通配符，在正则表达式里*表示匹配前面子表达式0次或者多次。）
    # 3. 由于sed的操作是以行为单位，在处理完所有行之后取出第一行的时间。
    #
    # 输入： <OMeS><PMSetup startTime="2017-07-10T18:45:00.000-04:00:00" interval="15">
    # 输出： "2017-07-10T18:45:00.000-04:00:00"
    #
    # 4. 最后是将最后一行两边的引号删掉。

		cat $1"/"$file | sed 's/measurementType/AAAAmeasurementType/g' | sed 's/AAAA/\n/g' | grep -i "LTE_M_per_LNCEL" > temp.txt
		cat temp.txt | grep -i 'LNCEL-1' > LNCEL-1.txt
		cat temp.txt | grep -i 'LNCEL-2' > LNCEL-2.txt
		cat temp.txt | grep -i 'LNCEL-3' > LNCEL-3.txt
    # 因为文件当中的数据是由 measurementType 开头进行组织，也就是每种Type下有对应的数据。所以在其前添加换行符 \n 来分割它们。
    # 之后通过关键字过滤出不同LNCEL的数据并分装在不同文件中。


		for((j=1;j<=3;j++));do
			InputFile=LNCEL-$j.txt
			OutputFile=LNCEL-$j.stat
			ParseCounter
      # 循环处理所有的文件，调用函数。
		done
	fi
done

cp LNCEL-1.stat LNCEL-1.csv
cp LNCEL-2.stat LNCEL-2.csv
cp LNCEL-3.stat LNCEL-3.csv
# 文件重命名。
```
