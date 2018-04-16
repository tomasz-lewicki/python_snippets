import threading
import time
import random


def get_time(name):
    print("Thread {} sleeps at {}".format(name,time.strftime("%H:%M:%S", time.gmtime())))

    rand_sleep_time = random.randint(1,5)

    time.sleep(rand_sleep_time)


class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        get_time(self.name)

        print("Thread", self.name, " execution ends")

thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive: ", thread1.is_alive())
print("Thread 2 Alive: ", thread2.is_alive())

print("Thread 1 Name: ", thread1.getName())
print("Thread 2 Name: ", thread2.getName())

thread1.join()
thread2.join()

print("Execution ends ")