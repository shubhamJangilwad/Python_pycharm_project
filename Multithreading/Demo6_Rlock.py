import threading

lock = threading.RLock()

def show():
    lock.acquire()
    print("show running...")
    print("counter 1")

    lock.acquire()
    print("counter 2")

    lock.release()
    print("counter 2")
    lock.release()
    print("counter 1")

show()