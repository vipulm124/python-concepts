import threading
import time


def worker():
    print('Worker thread started')
    time.sleep(10)
    print('Worker thread ended')

thread = threading.Thread(target=worker)
thread.start()

print("Main thread continues")
# thread.join() # this line is to make sure that everything post this line is only executed once the "thread" is complete
print("Post all thread ended")

# output is:
# Worker thread started
# Main thread continues
# Worker thread ended