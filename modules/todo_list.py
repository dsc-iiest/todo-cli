from .todo import todo
import heapq


class todo_list:
    """
    - The To-do List Object which stores the To-do in a Priority Queue (Heap).
    - Heap is based on lowest datetime first to get easy access to most current
    incoming To-do
    """

    def __init__(self) -> None:
        self.data = []

    def add_todo(self, task: str, deadline_offset: float = 1) -> None:
        """
        adds a to-do in the todo_list

        Parameters:
        task (str): the task of the todo
        deadline_offset (float): after how many min do you need to-do notify?
        """
        heapq.heappush(self.data, todo(task, deadline_offset))

    def curr_todo_done(self):
        """
        Call this when the most current event is done, this will delete
        that to-do from the list
        """
        heapq.heappop(self.data)

    def get_next_todo(self):
        """
        Return the next upcoming To-do in the todo list

        Returns: To-do Object
        """
        try:
            return self.data[0]
        except IndexError:
            print('Todo List is empty, consider adding some Todo')

    def list_size(self):
        """Returns the size of the to-do list"""
        return len(self.data)
