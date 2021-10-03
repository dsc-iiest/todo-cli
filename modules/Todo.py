import datetime


class Todo:
    """
    A single to-do with a task and a deadline
    """

    def __init__(self, task: str, offset: float):
        """
        Makes a To-do

        Parameters:
        task (str): the task of the To-do
        deadline_offset (float): after how many min do you need to-do notify?
        """
        self.time_rec = datetime.datetime.now() + datetime.timedelta(minutes=offset)
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
