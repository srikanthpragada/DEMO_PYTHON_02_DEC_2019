

import threading
from threading import Thread

def print_numbers():
    for i in range(1,10):
        print("Child : ",i, flush=True)

print(threading.main_thread())
t1 = Thread(target=print_numbers)
t1.start()

for i in range(1,10):
    print("Main ",i, flush=True)

print("\nWaiting for child to terminate!\n")
t1.join()   # Wait until child is terminated
print("\nThe End\n")