## HTML


## Q&A

1.outlook 对于html的支持似乎不是很好

今天调试comments日报，发现当使用两个div来布局的时候Outlook无法渲染第二个div里面的元素，在Firefox上面测试是可以的。当我将两个div合并为一个的时候outlook可以正常渲染。

在下面的第一篇参考文章（2019年）里面提到了Outlook HTML邮件在当时仅仅支持使用`<table>`来布局的情况：

> HTML emails have always been developed using <table> elements, and only <table> elements. Until now. The fact is, only Microsoft Outlook requires you to use tables for HTML structure; all other email and webmail clients support the use of <div>s for this purpose.

在第二篇参考文章里面也有下面的建议：

> If you want to successfully design a functional email, you’re going to have to design it like you’re living in 1999. In other words, you’re going to have to use table tags instead of div tags.
>
> The simple fact is this: Coding for the web is not the same as coding for HTML emails. An email is a space of approximately 600px and you have to include a lot of information in that small amount of space. It’s a fixed-width layout, whereas webpages offer more freedom.


参考：

- [Developing HTML Emails Using Divs and “Ghost Tables”](https://webdesign.tutsplus.com/tutorials/html-email-using-ghost-tables--cms-32551)
- [Ask a Designer: Tables or Divs for Email?](https://www.campaignmonitor.com/blog/email-marketing/ask-a-designer-tables-or-divs-for-email/)
