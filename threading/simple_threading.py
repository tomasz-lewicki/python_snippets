#!/usr/bin/python

import threading
import time
import random

ITERATIONS = 10000
list_of_times =[]
list_of_active_threads=[]


def count_to_million(thread_id):
    '''
    this function counts to 10 milion and print outs:
    -thread id
    -time that it took to execute
    '''
    start_time=time.time()

    #print("Thread {} starts counting at {}".format(thread_id, time.strftime("%H:%M:%S", time.gmtime())))

    for i in range(100000):
        i=i+1

    #print("Thread {} stops counting at {}".format(thread_id, time.strftime("%H:%M:%S", time.gmtime())))

    exec_time = time.time() - start_time

    list_of_times.append(exec_time)
    list_of_active_threads.append(threading.active_count())


def random_sleeping(thread_id):
    '''
    function exectues time.sleep for a random number of seconds between 1 and 5
    print outs its thread_id and time it took to execute
    '''

    #print("Thread {} goes to sleep at {}".format(thread_id,time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1,5)

    time.sleep(randSleepTime)

    #print("Thread {} stops sleeping at {}".format(thread_id, time.strftime("%H:%M:%S", time.gmtime())))


for i in range(ITERATIONS):
    thread = threading.Thread(target=random_sleeping,args=(i,))
    thread.start()

    thread2 = threading.Thread(target=count_to_million, args=(100+i,))
    thread2.start()

    print("started threads {} and {}".format(i,100+i))

    #print("There aere {} actvie threads: ".format(threading.active_count()))

#wait until there's just main thread
while(threading.active_count() != 1):
    time.sleep(1)

#calculate some stats
average_exec_time = sum(list_of_times)/len(list_of_times)
average_threads_count=sum(list_of_active_threads)/len(list_of_active_threads)

print("Average execution time from {} iterations is {}".format(ITERATIONS,average_exec_time))
print("Average thread count from {} iterations is {}".format(ITERATIONS,average_threads_count))

