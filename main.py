from modules.todo_list import todo_list
from modules.todo_list_checker import checker
import threading
import time

# This is a sample intended application of the todo-cli

if __name__ == "__main__":
    t = todo_list()
    # This will be done via interactive CLI (WIP)
    t.add_todo('Hello', 1.5)
    t.add_todo('Hello1', 0.5)
    t.add_todo('Hello2', 1)

    # multithread used here st it doesn't interfere with Future Todo Insertion
    t1 = threading.Thread(target=checker, args=(t, ), name='t1')
    # this makes the thread auto close when the parent thread closes
    t1.setDaemon(True)
    t1.start()

    # WIP: as there should be a Interactive CLI, there will be something
    # similar to an infinite loop with KeyboardInterrupt/exit() close
    # here this is simulated as a sleep timer
    time.sleep(100)
