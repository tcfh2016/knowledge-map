import pandas as pd

df = pd.read_csv("000898.csv", encoding="gb2312", dayfirst=True, usecols = ["日期", "收盘价"])
df = df[df["收盘价"] > 0]

df["日期"] = pd.to_datetime(df["日期"])
df["年"] = df["日期"].dt.year
df["月"] = df["日期"].dt.month

month_groups = df.groupby(["年", "月"])
#summed_groups = month_groups.sum()
month_groups.min().reset_index().to_csv("000898_month_min.csv", sep=',', encoding='gb2312')
month_groups.max().reset_index().to_csv("000898_month_max.csv", sep=',', encoding='gb2312')

print(month_groups)
