import threading
import time

lock = threading.Lock()

x = 0
def show():
    global x
    for i in range(5):
        lock.acquire()
        x += 1
        print(x)
        lock.release()

t1 = threading.Thread(target=show)
t2 = threading.Thread(target=show)

t1.start()
t2.start()



sem = threading.Semaphore(3)

def show(num):
    sem.acquire()
    print(num,"entered..")
    time.sleep(3)
    print(num,"leaving..")
    time.sleep(3)
    sem.release()

for i in range(5):
    t3 = threading.Thread(target=show,args=(i,))
    t3.start()


