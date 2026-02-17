import threading
# Two threads modify the same variable it is race condition
# To prevent race condition we use Lock
#
counter = 0
lock = threading.Lock()
def add():
    global counter
    for i in range(10):
        with lock:
            counter += 1
            print("running",threading.currentThread().name) # current running thread name

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)





