import threading

COUNT = 5000000
global FLAG
FLAG=10
shared_resource_with_lock = 0
shared_resource_with_no_lock = 0

shared_resource_lock = threading.Lock()

def increament_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()
        # print(threading.current_thread().getName(), FLAG)


def decreament_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -=1
        shared_resource_lock.release()
        # print(threading.current_thread().getName(), FLAG)
    

if __name__ == "__main__":
    t1 = threading.Thread(
        name='increament',
        target=increament_with_lock,
    )

    t2 = threading.Thread(
        name='deacremant',
        target=decreament_with_lock,
    )

    t3 = threading.Thread(
        name='increament',
        target=increament_with_lock,
    )

    t4 = threading.Thread(
        name='deacremant',
        target=decreament_with_lock,
    )


    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # To check whether the variable changes its value or not 

    print(f" shared_resource_with_lock : {shared_resource_with_lock}")


