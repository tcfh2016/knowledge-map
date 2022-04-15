## 需求二

需要对如下字符串进行解析：

> benchmark info : EMStart 2646861386,EMPreStart 2646861583,EMPreEnd 2646866714,EMSchStart 2646866770,EMSchEnd 2646870739,EMPostStart 2646870780,EMPostEnd 2646871748,total 10362,hasSib1 0,hasSibx 0,hascatmue 0

对比需求一、需求二，可以发现它们有共通的地方，即主体流程基本一致，但具体针对行解析的地方
是不一样的。因此重新改写。

## 需求一

2017年11月9日10:39:34

当前需要针对比较多的日志进行分析统计，尽管之前已经可以使用shell脚本来完成类似的工作，但
是由于当前不少工作在Windows平台下，考虑到便捷，因此决定使用Python来写作提取脚本。

需求：

>针对L2的一些日志进行分析，比如：
>FSP-124A-Disp_2 <2017-11-01T21:13:02.154659Z> 3A WRN/LTE L2/L2TupuDl/cB4F2r92BBu18CAx49DlF/MAC sent MAC_RlcDataSendResp with cause=MaxRlcRetransExceeded. Sending Tup_ErrorInd drbId=4
>其中的`cB4F2r92BBu18CAx49DlF`分别包含了不同的信息，要对它们进行分解。

成品：

```
from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Keywords.
keyword = "MaxRlcRetransExceeded"

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + ".csv"

def doParse(line):
    target_start = line.find("L2TupuDl/") + len("L2TupuDl/")
    target_end = line.find("/MAC")
    target = line[target_start:target_end]
    print (target)

    cStart = target.find('c')
    rStart = target.find('r')
    uStart = target.find('u')
    xStart = target.find('x')
    lStart = target.find('l')

    cellId  = int(target[cStart+1:rStart], 16)
    crnti   = int(target[rStart+1:uStart], 16)
    ueId    = int(target[uStart+1:xStart], 16)
    ueIndex = int(target[xStart+1:lStart], 16)
    lcid    = int(target[lStart+1:], 16)

    output_line = str(cellId) + "," + str(crnti) + "," + str(ueId) + "," + str(ueIndex) + "," + str(lcid) + "\n"
    print (output_line)
    return output_line

def main():
    output_fp = open(output_filename, 'w')
    with open(input_filename) as input_content:
        head_line = "cellId," + "crnti," + "ueId," + "ueIndex," + "lcid\n"
        output_fp.write(head_line)
        for line in input_content:
            if keyword in line:
                #print (line)
                output = doParse(line)
                output_fp.write(output)

    output_fp.close()

main()

```

一个感觉：发现Python写起来真的超级快，比shell都快很多。
