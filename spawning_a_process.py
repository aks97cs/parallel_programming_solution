""" simple way to spawn a process """
import multiprocessing

def function(i):
    print(f"called function in process {i}\n")
    return

if __name__ == "__main__":
    process_job = []
    for i in range(5):
        p = multiprocessing.Process(
            target=function,
            args=(i, ),
        )
        process_job.append(p)
        p.start()
        p.join()