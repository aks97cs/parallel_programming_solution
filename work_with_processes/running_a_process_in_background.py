import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print(f"staring {name}\n")
    time.sleep(3)
    print(f"ending {name} \n")
    

if __name__ == "__main__":
    background_process = multiprocessing.Process(
        target=foo,
        name='background_process',
    )
    # make daemon is True to run a process in background 
    background_process.daemon = True

    No_background_process = multiprocessing.Process(
        target=foo,
        name='No_background_process',
    )
    
    No_background_process.daemon = False
    background_process.start()
    No_background_process.start()
    
    background_process.join()
    No_background_process.join()