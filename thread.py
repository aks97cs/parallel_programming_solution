import threading

def function(i):
    print(f"function called by thread {i} \n")
    return

threads = []
for i in range(5):
    t = threading.Thread(
        target=function,
        args=(i, )
    )
    threads.append(t)
    t.start()
    t.join() # wait until the current thread is in execution