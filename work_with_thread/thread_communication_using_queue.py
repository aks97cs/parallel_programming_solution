from threading import Thread, Event
from queue import Queue
import time
import random


class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item) # put an item in Q
            print ('Producer notify : item N° %d appended to queue by %s \n'\
                   % (item, self.name))
            time.sleep(1)




class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get() # remove and return an item from Q
            print ('Consumer notify : %d popped from queue by %s'\
                   % (item, self.name))
            self.queue.task_done() # need to call each time an item has been process


if __name__ == '__main__':
        queue = Queue()
        t1 = producer(queue)
        t2 = consumer(queue)
        t3 = consumer(queue)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
