## 回声测试

20151122
今天周六，复习一下上周六在开发上面获得的新知识点。

在服务号申请成功之后，要想接入开发者进行其他功能的开发需要首先在开发中心上面进行配置。在配置当中需要填写自己的服务器地址，该地址用来处理微信服务器转发过来的“用户消息与点击事件”。上周六折腾了几个小时主要将服务器认证通过了。这将意味着微信服务器确定了转发用户消息与事件的地址。

今天主要想完成消息回文的测试，也就是验证用户输入->微信服务器->自己服务器->微信服务器->用户整个过程。还是参照官方文档与上周查询到的一个例子：

http://my.oschina.net/yangyanxing/blog/159215

不过，为在这里进行不下去了。因为上面链接当中的例子与当前已经实现的例子有些不一样，虽然知道大致怎么回事，但无法把验证的逻辑与消息处理的逻辑分隔开。无奈继续翻看《Pythen web开发学习实录》，在P343看到这么一段话：
CGI脚本文件通过环境变量、命令行参数和标准输入/输出流与HTTP服务器进行通信，传递参数并对该参数进行处理。当传递的方式为GET时，CGI程序通过环境变量来获取客户端提交的数据;当传递方式为POST时，CGI程序将通过标准输入流和环境变量来获取客户端提交的数据。当CGI程序返回处理结果给客户端时，则是通过标准输出流将数据输出到服务器进程中。
另外，在廖雪峰的这篇笔记里面看到，验证是GET方式，而其他的消息则是通过POST方式（这篇文章写于2014年1月份，未知当前是否依然如此，去查看上周的日志确认验证采取的方式未果），那么也就意味着将“验证”与“消息”分开得在这方式上面进行区分。

普及一下：GET与POST的传递方式区别在hyddd写的这篇总结里面讲得很到位：简单地说Get是向服务器发索取数据的一种请求，而Post是向服务器提交数据的一种请求，在FORM（表单）中，Method默认为"GET"。

在9秒社团这里找到了一份比较完整的参考代码，但是弄不清楚使用的web与baidu bae上面默认的wsgi有什么不一样。粗略看起来web上面直接有针对GET/POST的处理，但是wsgi上面有么？

还是看WSGI的主页指导得到的信息快，在这里即使用了解析POST的方式，那么也就是在通过REQUEST_METHOD区分了请求方式之后，对于POST消息的处理可以通过environ['wsgi.input']来取得POST的内容，一如在使用其他例子中使用web.data()来获取POST数据的处理一样。


## 初始配置


20151114
开始进入到公众号后台的开发人员模式，并按照开发文档中的接入指南进行服务器的最初设置，这一步在设置好了之后提示“token验证失败”，仔细阅读接入指南之后发现上面提到“填写的URL需要正确响应微信发送的token验证”：


对于web上面的交互一直没有认真了解过，幸好在上个月买了两本python web开发的书籍，略微一翻发现《Python Web开发学习实录》中的第12章正是可以参考的内容。

CGI的关键概念
CGI的全称为Common Gateway Interface，它定义了HTTP服务器和程序之间交换信息的规范，是外部应用程序和HTTP服务器之间交互的一个通用接口标准。既然是一个标准，所以在实现上与语言无关，Python自然是支持的。

在这里找到一个解决方案：

http://blog.csdn.net/trbbadboy/article/details/10709925

方案有问题：
1. 使用hashlib.sha1的时候不用包含hashlib模块
2. 使用re的时候不包含re会提示：
        Load module failed
  File "/home/bae/app/index.py", line 31

    body=["Welcome to Baidu Cloud!2\n"]

       ^

SyntaxError: invalid syntax
3. 搞了两三个小时总算认真成功了。简单记录下解决的主要问题：
》在搜索一些笔记，特别是廖雪峰的这篇文章，掌握了主要的验证机制。
》打开python，对token认证里面的代码逻辑进行验证。
   1. 验证是否必须要import os, hashlib, re，确定代码的语句没问题之后必须import hashlib,re
   2. ''.join在单引号当中不能有空格，因为这个时候是将排序好的几个元素拼接为一个字符串再生成sha1
   3
》发现在duapp上面的日志查看方式，有accesslog, errlog，从accesslog当中可以得知客户端发送过来的数据。

另外翻开《Python编程入门》学习了元组与列表区别，以及字典。参考代码在这里，最终代码如下：


#-*- coding:utf-8 -*-
import hashlib
import os
TOKEN = 'vooproject'

def check_signature(paras):
    global TOKEN
    signature = paras['signature']
    timestamp = paras['timestamp']
    nonce = paras['nonce']

    array = [TOKEN, timestamp, nonce]
    array.sort()
    temp_str = ''.join(array)
    temp_str = hashlib.sha1(temp_str).hexdigest()

    if (temp_str == signature):
        return paras['echostr']
    else:
        return ''

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    query_string = environ['QUERY_STRING']
    all_parameters = dict(re.findall('([^=, ^&, ^?]*)=([^=, ^&]*)',query_string)

    #body=["Welcome to Baidu Cloud!\n"]
    return check_signature(all_parameters)

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)




2015年10月21日19:33:24
准备开始做第一个微信公众号的开发项目，为一初中同学做。

知乎文章
http://www.zhihu.com/question/20956354

http://www.zhihu.com/question/23644489/answer/25230137

官方开发文档
http://mp.weixin.qq.com/wiki/home/index.html

入门指导
http://www.cnblogs.com/mchina/archive/2013/06/05/3108618.html
http://www.cnblogs.com/txw1958/p/wechat-tutorial.html

购买百度云服务
http://console.bce.baidu.com/bae/#/bae/env/create

示例代码：
http://mp.weixin.qq.com/wiki/9/aaa4ddd9bbf36b1479a36cbcb00060c1.html


看了百度，腾讯，阿里的云服务，各种不懂。一个：应用引擎与云服务器区别是什么呢？查了下大致是云引擎基本是已经给你做好了一些基础功能，而云服务器需要你自己配置很多东西。那还是选择云引擎了。
