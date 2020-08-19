"""
re模块功能扩展标志
"""
s = """Hello world
北京 你好
"""
import re

# 让^,$ 表示每一行的开头结尾位置
result = re.findall(r"\w+$", s, flags=re.M)
print(result)
# 执行结果['world', '你好']


# 让大小写通用，忽略字母大小写
result = re.findall(r"[a-z]+", s, flags=re.I)
print(result)
# 执行结果['Hello', 'world']


# 让. 匹配换行符
result = re.findall(r".+", s, flags=re.S)
print(result)
# 执行结果


# 让正则表达式只能匹配英文字符
result = re.findall(r"\w+", s, flags=re.A)
print(result)
# 执行结果['Hello', 'world']
