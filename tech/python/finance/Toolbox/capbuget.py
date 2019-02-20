def npv(list, rate):
    T = 0
    sum = 0
    for v in list:
        T += 1
        sum += v / ((1 + rate)**T)
        #print("期数" + str(T) + " 金额：" + str(v) + ", 总计：" + str(sum) + "\n")
    return sum
