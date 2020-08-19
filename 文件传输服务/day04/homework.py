import re

# 方法一：
port = input('请输入端口名称：')
file = open("log.txt", "r")
a = file.read()
list01 = re.split(r"\n\n", a)
for item in list01:
    list02 = re.split(" ", item)
    c = list02[0]
    if c == port:
        b = re.search(r"\w+[a-z]+\w+\.\w+\.\w+", item)
        if b:
            print(b.group())
        else:
            print("该端口没有adress!")

"""
# 方法二：
# 获取一段：
def get_info():
    file01 = open("log.txt")
    while True:
        data = ""
        for line in file01:
            if line == "\n":
                break
            data += line
        if not data:
            file01.close()
            return
        yield data


# 获取地址：
def get_adress():
    name = input("接口名称：")
    for info in get_info():
        obj = re.match(r"\S+", info)
        if name == obj.group():
            pattern = r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            result = re.search(pattern, info)
            if result:
                print(result.group())
            else:
                print("Unknow")
            return
    else:
        print("没有该端口！")

get_adress()
"""
