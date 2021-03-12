name = "hello i am jianwei99"
#title() 将每个单词的首字母都改成大写
print(name.title())
#upper() 所有字符大写
print(name.upper())
#lower() 所有字符小写
print(name.lower())

first_name = "Jw"
last_name = "Han"
#使用加号"+"来合并字符串
full_name = first_name + " " + last_name
print("This guy full name is " + full_name + "\nHello, " + full_name + "!")
message = "This guy full name is  ".rstrip() +" "+ full_name
'''
rstrip()用于删除字符串末尾的空白字符
lstrip()用于删除字符串开头的空白字符
strip()用于删除字符串两端的空白字符
eg.
>>>name = " John "
>>>name.lstrip()
'John '
>>>name.rstrip()
' John'
>>>name.strip()
'John'
'''
print(message)
