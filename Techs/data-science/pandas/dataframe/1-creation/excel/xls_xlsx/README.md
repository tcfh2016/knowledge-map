## `.xls`和`.xlsx`


.xls格式是Office 2003及之前版本的Excel文件的格式，我们在使用pandas里面的`read_excel()`和`to_excel()`读取和保存。xls格式的时候需要安装对应的函数库：

- 读.xls需要安装`xlrd`函数库
- 写.xls需要安装`xlwt`函数库

Office 2007及之后版本的Excel文件是.xlsx格式，读取.xlsx格式的电子表格需要的函数库又不同了，是`openpyxl`。

所以，如果你还在操作.xls格式，那么就会收到有关`xlrd`/`xlwt`函数库过时不再维护的信息。