filename1 = "关键词搜索次数排名_关键字.csv"
filename2 = "搜索进入详情页pv排名_关键字.csv"

line = []

# 定义一个函数，从一个文件里面从前往后读取行，并保存在变量 line里面
def proc_file(filename):
    # 定义两个计数用的变量，用来控制读取的行数，以及统计重复行的个数
    cnt1 = 0
    cnt2 = 0

    # 打开文件，并将文件内容读取保存起来，然后遍历其中的每行
    f = open(filename, 'r', encoding="utf-8")
    for word in f:
        # 每读取一行就让计算变量cnt1递增1，当超过500的时候就不要读取了
        cnt1 += 1
        if cnt1 > 500:
            break
        # 对于每行，先去除前后的空格，并判断line里面是否已经包含了该行（关键字）
        # 如果包含了那么就让计算变量cnt2递增1，否则就添加到line里面
        word = word.strip()
        if word not in line:
            line.append(word)
        else:
            cnt2 += 1
    f.close()

    print("取了文件{0}中{1}个关键字，其中重复关键字{2}个。".format(filename, cnt1-1, cnt2))

# 定义另外一个函数，将line里面保存的关键字逐个读出，并且在每个关键字后面添加逗号
# 然后写入summary.txt文件
def write_file():
    print("即将写入{0}条记录".format(len(line)))
    content = ""
    for w in line:
        content += (w + ',')

    f = open("summary.txt", 'w', encoding="utf-8")
    f.write(content)
    f.close()

# 调用函数，分别处理第一个文件，第二个文件，然后再写文件保存结果
proc_file(filename1)
proc_file(filename2)
write_file()
