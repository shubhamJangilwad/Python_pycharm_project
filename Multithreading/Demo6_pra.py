import threading
import time

def show():
    print("Hello")

def show1():
    print("Python")

t1 = threading.Thread(target=show)
t2 = threading.Thread(target=show1)
t1.start()
t2.start()


def show3():
    for i in range(1,6):
        print(i,threading.current_thread().name)
        time.sleep(1)

t3 = threading.Thread(target=show3)
t3.start()
t3.join()
print("Done")




lock = threading.Lock()
def show4():
    for i in range(1,11):
        if i%2==0:
            with lock:
                print("even:",i)
                time.sleep(0.5)


def show5():
    for i in range(1,11):
        if i%2!=0:
            with lock:
                print("odd",i)
                time.sleep(0.5)

t4 = threading.Thread(target=show4)
t5 = threading.Thread(target=show5)
t4.start()
t5.start()
t4.join()
t5.join()



lock = threading.Lock()
counter = 0
def show6():
    global counter
    for i in range(100000):
            counter += 1

t6 = threading.Thread(target=show6)
t7 = threading.Thread(target=show6)
t6.start()
t7.start()
t6.join()
t7.join()
print(counter)
