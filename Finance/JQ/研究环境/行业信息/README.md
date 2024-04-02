## 行业列表：`get_industries`

```
from jqdata import *
get_industries(name, date=None)
```

name表示行业代码：

"sw_l1": 申万一级行业
"sw_l2": 申万二级行业
"sw_l3": 申万三级行业
"jq_l1": 聚宽一级行业
"jq_l2": 聚宽二级行业
"zjw": 证监会行业


## 股票所属行业：`get_industry`

```
get_industry(security, date=None)
```

可以支持同时查询多个证券，返回都是以字典形式返回，每个标的会对应多个行业分类的信息。

```
{'002236.XSHE': {'jq_l1': {'industry_code': 'HY008', 'industry_name': '信息技术'},
  'zjw': {'industry_code': 'C39', 'industry_name': '计算机、通信和其他电子设备制造业'},
  'sw_l1': {'industry_code': '801750', 'industry_name': '计算机I'},
  'sw_l3': {'industry_code': '850702', 'industry_name': '安防设备III'},
  'sw_l2': {'industry_code': '801101', 'industry_name': '计算机设备II'},
  'jq_l2': {'industry_code': 'HY08109', 'industry_name': '安防设备及其他'}}}
```



参考

- [行业概念数据](https://www.joinquant.com/help/api/help#name:plateData)
- [API新](https://www.joinquant.com/help/api/help#api:get_industries)
- [](https://www.joinquant.com/help/api/help?name=api#get_industry)