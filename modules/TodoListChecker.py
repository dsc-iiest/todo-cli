from .TodoList import TodoList
from .Notifier import send_notification
import datetime
import time


def checker(todo_lst: TodoList):
    """
    Check if any to-do from the to-do list has passed it's deadline or not

    Parameters:
    todo_lst (todo_list): the todo_list object

    Returns:
    None
    """
    try:
        while True:
            while todo_lst.list_size() > 0:
                t = todo_lst.get_next_todo()
                if datetime.datetime.now() >= t.get_deadline():
                    t.deadline_reached()
                    send_notification(t)
                    todo_lst.curr_todo_done()
            time.sleep(60)
    except KeyboardInterrupt:
        exit()
