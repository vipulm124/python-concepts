import multiprocessing
import time

def background_task():
    """Function to be run in the background process."""
    for i in range(10):
        print(f"Background task: {i}")
        # Pause for 0.5 seconds between each iteration
        time.sleep(1)

def front_task():
    letters = "ABCDEFGHI"
    for letter in letters:
        print(f"Letter: {letter}")
        time.sleep(0.5)

if __name__ == '__main__':
    # Create a process to run the background task
    background_process = multiprocessing.Process(target=background_task)

    # Start the background process
    background_process.start()

    front_task()

    # Wait for the background process to complete before exiting the program
    background_process.join()