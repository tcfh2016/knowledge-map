# 当前为第0期，计算从第1期开始到第N期所得现金的折现值。
def pv(list, rate):
    T = 0
    sum = 0
    for v in list:
        T += 1
        sum += v / ((1 + rate)**T)
    return sum
