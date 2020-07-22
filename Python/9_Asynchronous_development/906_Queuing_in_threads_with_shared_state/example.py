
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489768#overview
# i just copy paste this example from the training as its a bit complex
# the programs runs and prints just once and then it stops. Don't know why. its related to the module threads and queues

from threading import Thread
import time
import random
import queue

counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def increment_manager():
    global counter
    print ('Thread 1 to get increment is started')
    while True:
        increment = counter_queue.get()  # this waits until an item is available and locks the queue. If there are several threads waiting , just 1 can fetch one available item, and then the queue is locked until we unlock it.
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New counter value {counter}', '------------'))
        counter_queue.task_done()  # this unlocks the queue.

# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=increment_manager, daemon=True).start()

def printer_manager():
    print('Thread 2 for printing is started')
    while True:
        for line in job_queue.get(): # each thread will wait here until 1 value is available. If it does the first thread will get it and then the queue is locked.
            print(line)
            job_queue.task_done()

# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    print('Thread 3 that puts values in the queue is started')
    thread.start()

for thread in worker_threads:
    thread.join()  # wait for it to finish

counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty