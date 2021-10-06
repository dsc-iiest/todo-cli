from notifypy import Notify
from .Todo import Todo


def send_notification(t: Todo):
    notification = Notify()
    notification.title = t.get_task()
    notification.message = t.get_desc()
    notification.application_name = 'Todo-CLI'
    # notification.audio =
    # notification.icon =
    notification.send()
