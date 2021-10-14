import datetime


class Todo:
    """
    A single to-do with a task and a deadline
    """

    def __init__(self, task: str, desc: str, notification_datetime: datetime):
        """
        Makes a To-do

        Parameters:
        task (str): the task of the To-do
        desc (str): the description of the To-do
        notification_datetime (datetime): when do you need to-do notify?
        """
        self.time_rec = notification_datetime
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
        print(f"\nDeadline for task '{self.get_task()}' has been reached\n"
                f"Its description was: {self.get_desc()}\n")
        print("Enter Command below ('--help' for usage instructions "
                "or 'exit' to close):\n")

    def __lt__(self, other) -> bool:
        """less than operator override"""
        return self.get_deadline() < other.get_deadline()

    def __repr__(self) -> str:
        """representation override"""
        return f"todo:\n\tTask: {self.get_task()}\n\tDesc: {self.get_desc()}\n\tTime: {self.get_deadline()}"
