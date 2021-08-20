

## 搜索

- [文本搜索 / grep](./grep.md)

## 统计

- [统计/wc](./wc.md)

## 操纵

- [行处理/sed](./sed.md)
- [列处理/awk](./awk.md)
- [切分/split](./split.md)

```
# 搜索文件夹下.hpp包含"getRise()"的文件，并打印行号（-n）

find directory/ -name "*.hpp"|xargs grep -n getRise()

-path ./uplane/sdkuplane -prune -o

```

find directory/ -name "CCSEarlyConfig.xml"|xargs grep -n "<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>"

<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>
