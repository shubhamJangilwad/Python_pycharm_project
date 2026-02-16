import threading
import time

def show():
    for i in range(5):
        print("A",i)
        time.sleep(1)

def tell():
    for k in range(5):
        print("B",k)

s = threading.Thread(target=show)
t = threading.Thread(target=tell)
s.start()
t.start()

s.join()
t.join()
print("Done")