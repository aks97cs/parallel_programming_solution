import os
import sys

program = "python"
print("process calling ..")
arg = ["/home/anuj/mylearning/parallel_programming_solutions/workwithprocesses/called_process.py"]
os.execvp(program, (program,)+tuple(arg))