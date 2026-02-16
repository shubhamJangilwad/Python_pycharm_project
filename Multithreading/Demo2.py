import threading
import time


def start():
    for i in range(10):
        print("python")
        time.sleep(1)


t1 = threading.Thread(target=start)

t1.start()
t1.join()

print("main finished")