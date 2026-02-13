import threading
import time

def task1():
    print("This is laptop")



t = threading.Thread(target=task1)
t.start()




def task():
    for i in range(3):
        print("Task", i)
        time.sleep(1)

t = threading.Thread(target=task)

print("Using run()")
t.run()

print("Using start()")
t = threading.Thread(target=task)
t.start()
