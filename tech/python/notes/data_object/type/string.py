import re


# strip方法
s = 'http://www.python.org/'
print(s.strip('htp:/'))

# 正则展示
series = """
         '01/18/2014 13:00:00', 100, '1st';
         '01/18/2014 13:30:00', 110, '2nd';
         '01/18/2014 14:00:00', 120, '3rd'
         """
date_time_regx = re.compile("'[0-9/:\s]+'")
date_time_strs = date_time_regx.findall(series)

print(date_time_strs)


h1 = 'he said: "hello!"'
h2 = 'he said: \"hello!\"'
h3 = "It's fine!"
h4 = "It\'s fine!"
h5 = r'It\'s fine!'

print(h1, h2, h3, h4, h5)
