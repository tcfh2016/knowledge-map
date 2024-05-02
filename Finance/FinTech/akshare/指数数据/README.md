## 指数信息


```
import akshare as ak

# 国证指数（深交所指数机构）
index_all_cni_df = ak.index_all_cni()
print(index_all_cni_df)

# 所有常用指数
index_stock_info_df = ak.index_stock_info()
print(index_stock_info_df)
```

## 指数成分 

```
import akshare as ak

index_stock_cons_df = ak.index_stock_cons(symbol="000300")
print(index_stock_cons_df)
```

## 指数估值

1）中证指数

```
import akshare as ak

stock_zh_index_value_csindex_df = ak.stock_zh_index_value_csindex(symbol="H30374")
print(stock_zh_index_value_csindex_df)
```

2）国证指数

```

```

3）韭圈儿


```
import akshare as ak

index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol="大盘成长", indicator="市盈率")
print(index_value_hist_funddb_df)
```