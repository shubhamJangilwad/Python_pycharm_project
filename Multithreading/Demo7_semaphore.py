import threading
import time

sem = threading.Semaphore(3)

def task(name):
    sem.acquire()
    print(name, "entered")
    time.sleep(4)
    print(name, "leaving")
    time.sleep(2)
    sem.release()

for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    t.start()