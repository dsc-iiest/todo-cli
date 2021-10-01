from .todo import todo
import heapq

class todo_list:
    '''
    The Todo List Object which stores the Todo in a Priority Queue (Heap).
    Heap is based on lowest datetime first to get easy access to most current incoming Todo
    '''
    def __init__(self) -> None:
        self.data = []

    def add_todo(self, task: str, deadline_offset: float = 1)-> None:
        '''
        adds a todo in the todo_list

        Parameters:
        task (str): the task of the todo
        deadline_offset (float): after how many min do you need the todo notification?
        '''
        heapq.heappush(self.data, todo(task, deadline_offset))

    def curr_todo_done(self):
        '''Call this when the most current event is done, this will delete that todo from the list'''
        a = heapq.heappop(self.data)

    def get_next_todo(self):
        '''
        Return the next upcoming Todo in the todo list

        Returns: Todo Object
        '''
        try:
            return self.data[0]
        except IndexError:
            print('Todo List is empty, consider adding some Todo')

    def list_size(self):
        '''Returns the size of the todo list'''
        return len(self.data)