"""
event 线程同步互斥方法演示
"""
from threading import Thread, Event

msg = None
e = Event()  # 创建线程event对象


# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()  # 解除主线程阻塞


t = Thread(target=杨子荣)
t.start()
# 主线程验证
print("说对口令就是自己人!")
e.wait()  # 设置阻塞
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人!")
else:
    print("打死他!")

t.join()
