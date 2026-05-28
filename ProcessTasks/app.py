import time
import multiprocessing
import os
import threading

def main_another():
    print("This is the main function of app.py" )
    current_process = multiprocessing.current_process()
    current_process_id = os.getpid()
    print(f"Current Process ID: {current_process_id}")
    print(f"Current Process Name: {current_process.name}")
    time.sleep(3)



# if __name__ == "__main__":
main_another()
current_process = multiprocessing.current_process()
current_process_id = os.getpid()
print(f"Current Process ID: {current_process_id}")
print(f"Current Process Name: {current_process.name}")
current_thread = threading.current_thread()
main_thread = threading.main_thread()
print(f"Current Thread: {current_thread.ident}")
print(f"Main Thread: {main_thread.ident}")