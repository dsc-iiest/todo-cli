from .todolist import TodoList
import datetime
import time


def checker(todo_lst: TodoList):
    """
    Check if any todo from the todo list has passed it's deadline or not

    Parameters:
    todo_lst (todo_list): the todo_list object

    Returns:
    None
    """
    try:
        while(True):
            while(todo_lst.list_size() > 0):
                t = todo_lst.get_next_todo()
                if(datetime.datetime.now() >= t.get_deadline()):
                    print(t)
                    todo_lst.curr_todo_done()
            time.sleep(60)
    except KeyboardInterrupt:
        exit()
