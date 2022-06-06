## [定位页面元素](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

定位到页面元素的手段比较多，常见是就是下面这些方法：

```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```

举个例子，对于下面的输入框元素我们可以通过多种方法来找到它。

```
<input type="text" name="passwd" id="passwd-id" />

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")
```

XPath是专门应用在XML文档里面搜索节点的语言，XPath支持根据id, name来定位元素，即便某个元素没有id/name，也可以通过XPath进行绝对定位（通过绝对路径？）和相对定位（根据具有id/name的元素进行相对位置的定位），并且还可以支持根据attributes来定位元素。

可以通过F12打开浏览器的开发人员工具很快的定位到具体元素，比如在下图里面可以很快的拷贝到特定元素的XPth，比如我拷贝出“SING IN”按钮的XPath为`/html/body/main/section[1]/div[3]/div/a`。

![](./shortcut-for-XPath.png)

*问题：如果定位不到对应元素，对应的返回值和常见的处理方法是怎样的呢？*

在[3.1. Interacting with the page](https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page)讲解定位元素时如果找不到那么会抛出`NoSuchElementException`异常。

> You can also look for a link by its text, but be careful! The text must be an exact match! You should also be careful when using XPATH in WebDriver. If there’s more than one element that matches the query, then only the first will be returned. If nothing can be found, a NoSuchElementException will be raised.
