import pandas as pd

# 从原始文件里面读取"action", "cookie_id", "product_id" 三列进行分析。
df = pd.read_csv("用户行为数据统计0522.csv", encoding="gb2312", usecols = ["action", "cookie_id", "product_id"])

# 删除"action" 当中的 ‘click_phone’
#df = df[df['action'] != 'click_phone']

# 按照 cookie_id, product_id 进行分组，意思为：
#   1. 某个用户访问某个产品归入同一组。
#   2. 某个用户访问不同产品，以及不同用户访问同一产品均归为不同组。
user_access_group = df.groupby(["cookie_id", "product_id"])

# 统计用户访问产品页的次数，也就是 cookie_id <-> product_id 对应的个数。
user_access_times = user_access_group.size().size
print ("用户访问产品页的总次数：{:d}".format(user_access_times))

# 统计用户访问产品页的有效次数，即统计 click 的方式 “大于等于 2”的次数
valid_access_times = 0;
for name, user_access in user_access_group:
    actions = user_access.groupby(["action"]).size().size
    if actions >= 2:
        valid_access_times += 1
print ("用户访问产品页的有效次数：{:d}".format(valid_access_times))

print ("有效的访问次数占总的访问次数： {:.2%}".format(valid_access_times / user_access_times))
