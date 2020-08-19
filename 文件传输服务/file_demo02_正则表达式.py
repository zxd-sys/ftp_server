import re

"""
 实例
"""
s = """Alex:2000 Sunny:1999 Tom:2001"""
# 通过正则表达式获取
pattern = r"(\w+):(\d+)"
# pattern = r"\w+:\d+"
# pattern = r"(\w+):\d+"
# 如果正则表达式有子组，findall只返回子组对应匹配的内容
result = re.findall(pattern, s)
print(result)
# 分割
result01 = re.split(r"\s+", s)
print(result01)
# 替换
new = re.sub(r"\s+", "##", s)
print(new)
