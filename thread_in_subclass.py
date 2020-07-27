import threading
import time

flag = 0

class myThread (threading.Thread):

    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    
    def run(self):
        print(f"starting {self.name} \n")
        print_time(self.name, self.counter, 5)
        print(f"ending {self.name} \n")


def print_time(threadName, delay, counter):
    while counter:
        if flag:
            thread.exit()
        time.sleep(delay)
        print(f"{threadName} : {time.ctime(time.time())}")
        counter -= 1

if __name__ == "__main__":
    t1 = myThread(1, "thread-1", 1)
    t2 = myThread(2, "thread-2", 2)


    t1.start()
    t2.start()


    t1.join()
    t2.join()


    print("exiting main thread ..")