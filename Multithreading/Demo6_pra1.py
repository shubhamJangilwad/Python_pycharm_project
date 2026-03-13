import threading
import time

# def show():
#     print("running....")
#     time.sleep(3)
#     print(threading.current_thread())
#
# def move():
#     print("move running....")
#
# t1 = threading.Thread(target=show)
# t2 = threading.Thread(target=move)
#
# t1.start()
# t1.join()
# t2.start()
# print("main finished")
#
#
#
# # args passes
# def man(name):
#     print("your name "+name)
#
# t3 = threading.Thread(target=man, args=("shubham",))
# t3.start()
#
#
#
# # daemon thread
#
# def mouse():
#     print("shubham running.....")
#
# t4 = threading.Thread(target=mouse)
# t4.daemon = True #set daemon before starting the thread (t4.start())
# t4.start()
# t4.join()
# print("main finished")
# print("daemon end automatically")

lock = threading.Lock()
x = 0
def increase():
    global x
    for i in range(5):
        lock.acquire()
        x +=1
        print(x)
        lock.release()

t5 = threading.Thread(target=increase)
t6 = threading.Thread(target=increase)
t5.start()
t6.start()
t5.join()
t6.join()

