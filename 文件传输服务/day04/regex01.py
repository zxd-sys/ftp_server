import re

"""
 实例
"""
s = """Alex:2000 
    Sunny:1999 
    Tom:2001
    """
pattern = r"(\w+):(?P<age>\d+)"
result = re.finditer(pattern, s)
# 迭代取出的是每处匹配内容对应的match对象
for i in result:
    print(i.group())  # 获取对应的匹配内容
# 执行结果Alex:2000
# Sunny:1999
# Tom:2001

print("======================================")
# 匹配目标字符串的开头位置
obj = re.match(pattern, s)
print(obj.group())
# 执行结果Alex:2000
print("======================================")
# (0, 9)相当于s[0:9]包括9
print(obj.span())
# 执行结果(0, 9)
print("================================")
# 捕获组字典: {'age': '2000'}
print(obj.groupdict())
# 执行结果{'age': '2000'}
print("======================================")


# 只匹配目标字符串第一处符合正则表达式的内容
result01 = re.search(pattern, s)
print(result01.group())
print(result01.group(2))  # 组序号
print(result01.group("age")) # 组名字
# 执行结果Alex:2000
# 2000
# 2000


