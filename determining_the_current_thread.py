import threading
import time


def first_function():
    print(f"{threading.current_thread().getName()} is starting \n")
    time.sleep(2)
    print(f"{threading.current_thread().getName()} is ended \n")
    return


def second_function():
    print(f"{threading.current_thread().getName()} is starting \n")
    time.sleep(2)
    print(f"{threading.current_thread().getName()} is ended \n")
    return

def third_function():
    print(f"{threading.current_thread().getName()} is starting \n")
    time.sleep(2)
    print(f"{threading.current_thread().getName()} is ended \n")
    return


def forth_function():
    print(f"{threading.current_thread().getName()} is starting \n")
    time.sleep(2)
    print(f"{threading.current_thread().getName()} is ended \n")
    return


if __name__ == "__main__":
    t1 = threading.Thread(
        name='first_function',
        target=first_function,
    )

    t2 = threading.Thread(
        name='second_function',
        target=second_function,
    )

    t3 = threading.Thread(
        name='third_function',
        target=third_function,
    )

    t4 = threading.Thread(
        name='forth_function',
        target=forth_function,
    )

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()