"""
线程锁演示
"""
from threading import Thread, Lock
lock = Lock()
a = b = 0


def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %f,b= %f" % (a, b))
        lock.release()


t = Thread(target=value)
t.start()
while True:
    # with lock: with语句块执行后自动解锁
    lock.acquire()
    a += 0.1
    b += 0.1
    lock.release()

t.join()
