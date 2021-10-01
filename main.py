from modules.todo_list import todo_list
from modules.todo_list_checker import checker
import threading
import sys
import time

# This is a sample intended application of the todo-cli

if __name__ == "__main__":
    t = todo_list()
    # This will be done via interactive CLI (WIP)
    t.add_todo('Hello', 1.5)
    t.add_todo('Hello1', 0.5)
    t.add_todo('Hello2', 1)

    # multithreading used here st it doesn't interfere with Future Todo Insertion
    t1 = threading.Thread(target= checker,args=(t, ), name = 't1')
    t1.setDaemon(True) #this makes the thread auto close when the parent thread closes (this code)
    t1.start()

    # WIP: as there should be a Interactive CLI, there will be somthing similar to an infinite loop with KeyboardInterrupt/exit() close
    # here this is simulated as a sleep timer
    time.sleep(100)
