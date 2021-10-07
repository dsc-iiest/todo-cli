from notifypy import Notify
from .Todo import Todo


def send_notification(t: Todo):
    notification = Notify()
    notification.application_name = 'Todo-CLI'
    notification.title = t.get_task()
    notification.message = t.get_desc()
    # notification.audio =
    notification.icon = './icon.png'
    notification.send()
