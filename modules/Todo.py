import datetime


class Todo:
    """
    A single to-do with a task and a deadline
    """

    def __init__(self, task: str, desc: str, offset: float):
        """
        Makes a To-do

        Parameters:
        task (str): the task of the To-do
        deadline_offset (float): after how many min do you need to-do notify?
        """
        self.time_rec = datetime.datetime.now() + datetime.timedelta(minutes=offset)
        self.task = task
        self.desc = desc

    def get_task(self):
        """Return the task of the to-do"""
        return self.task

    def get_deadline(self) -> datetime:
        """returns the deadline"""
        return self.time_rec

    def get_desc(self) -> str:
        """return the To-do Description"""
        return self.desc

    def deadline_reached(self) -> None:
        """Print a message announcing that the todo's deadline is up."""
        print(f"\nDeadline for task '{self.get_task()}' has been reached - its"
                f" description was:\n\n{self.get_desc()}\n")

    def __lt__(self, other) -> bool:
        """less than operator override"""
        return self.get_deadline() < other.get_deadline()

    def __repr__(self) -> str:
        """representation override"""
        return f"todo:\n\tTask: {self.get_task()}\n\tDesc: {self.get_desc()}\n\tTime: {self.get_deadline()}"
