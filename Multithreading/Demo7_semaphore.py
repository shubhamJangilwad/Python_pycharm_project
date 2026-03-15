import threading
import time

sem = threading.Semaphore(3)

def task(num):
    sem.acquire()
    print(num, "entered")
    time.sleep(4)
    print(num, "leaving")
    time.sleep(2)
    sem.release()

for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    t.start()