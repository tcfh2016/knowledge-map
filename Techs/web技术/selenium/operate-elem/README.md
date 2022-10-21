## [操作页面元素](https://selenium-python.readthedocs.io/navigating.html)

操作定位到的元素主要包括输入、点击等。

1）对于文本框的操作

```
# 输入内容
element.clear()
element.send_keys("some text")
```

2）对于可选元素的操作

```
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

# 取消选择
select = Select(driver.find_element_by_id('id'))
select.deselect_all()

# 获取选择项
select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options
```

3）对于点击类型的按钮

```
# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()

# WebDriver 为每个element都提供了简便的submit函数来实现点击
element.submit()

# 点击
element.send_keys(" and some", Keys.ARROW_DOWN)
```

4）在Window和Frame之间移动

```
# 切换到某个window
driver.switch_to_window("windowName")

# 遍历每个打开的window
for handle in driver.window_handles:
    driver.switch_to_window(handle)

# 切换到某个frame
driver.switch_to_frame("frameName")

# 访问某个sub-frame
driver.switch_to_frame("frameName.0.child")
```

5）弹出的对话框

通过`alert = driver.switch_to.alert`可以访问弹出的alert对象，该接口也能够很好的访问confirm, prompt对象。
