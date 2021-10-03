import datetime


class todo:
    """
    A single todo with a task and a deadline
    """

    def __init__(self, task: str, offset: float):
        """
        Makes a Todo

        Parameters:
        task (str): the task of the Todo
        deadline_offset (float): after how many min do you need to-do notify?
        """
        self.time_rec = datetime.datetime.now() + datetime.timedelta(offset)
        self.task = task

    def get_task(self):
        """Return the task of the to-do"""
        return self.task

    def get_deadline(self) -> datetime:
        """returns the deadline"""
        return self.time_rec

    def __lt__(self, other) -> bool:
        """less than operator override"""
        return self.get_deadline() < other.get_deadline()

    def __repr__(self) -> str:
        """representation override"""
        return f"todo : {self.get_task()} @{self.get_deadline()}"
