# footer

footer 用来为文档或者区块定义页脚，里面通常包括：

- 作者信息
- 版权信息
- 联系信息
- 网站地图
- 相关文件

```
<footer>
  <p>Author: Hege Refsnes</p>
  <p><a href="mailto:hege@example.com">hege@example.com</a></p>
</footer>


footer {
  text-align: center;
  padding: 3px;
  background-color: DarkSalmon;
  color: white;
}
```

其实我不是很明白为什么一定要footer标签，其实也可以使用其他比如<p>, <div>这些，目前猜测仅仅是在语义上这么定义，语法上和其他标签并没有什么显见的不同。

参考：

- [HTML <footer> Tag](https://www.w3schools.com/tags/tag_footer.asp)
