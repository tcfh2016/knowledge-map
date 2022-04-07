## 用html编写outlook邮件

outlook能够支持的html特性是有限的，在[An Introduction To Building And Sending HTML Email For Web Developers](https://www.smashingmagazine.com/2017/01/introduction-building-sending-html-email-for-web-developers/)可以看到一些推荐用法，即便布局也推荐使用`table`而非`div`：

```
<table> instead of <div>,
#FFFFFF instead of #FFF,
padding instead of margin,
CSS2 instead of CSS3,
HTML4 instead of HTML5,
background-color instead of background,
HTML attributes instead of CSS,
inline CSS instead of style sheets or <style> blocks.
```

## Q&A

1) table无法居中的问题

今天一直在调试comments报告的格式，在浏览器里面显示没有问题，但是在outlook里面还是左对齐，没有办法居中显示。之后定位到和`captaion`有关：

- 使能语句A，注释语句B的时候没有办法居中
- 使能语句B，注释语句A的时候可以正常居中，但是这个时候该表格的标题名称"Open Review List"会显示到整个邮件开头，明显是不对的

```
def print_open_review(open_list):
    print ('<tr>')    
    print ('<td style="border:0px;">')
    #print ('<h3 style="margin:0 auto">Open Review List</h3>') -- A
    print ('<table class="table_reviews_section">')
    #print ('<caption><h3>Open Review List</h3></caption>') -- B
```

之后google后在[What's the best way to center your HTML email content in the browser window (or email client preview pane)?](https://stackoverflow.com/questions/2857765/whats-the-best-way-to-center-your-html-email-content-in-the-browser-window-or)找到了解决方案，即在最外层的table里面添加`align='center'`，比如`<table align="center" style="border:0px; margin:auto; background-color:AliceBlue; text-align:center;"> `。
