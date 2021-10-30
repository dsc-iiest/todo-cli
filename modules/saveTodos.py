import json
from cryptography.fernet import Fernet
import datetime
import os

from .TodoList import TodoList


KEY_FILE = 'key'
DATA_FILE = 'dump.dat'


def get_key():
    if KEY_FILE in os.listdir('.'):
        return open('./key', 'rb').read()
    else:
        key = Fernet.generate_key()
        with open('./key', 'wb') as f:
            f.write(key)
        return key


def save_data(t: TodoList):
    data = {}
    data['todo'] = []
    for i in t.data:
        task = i.get_task()
        desc = i.get_desc()
        time = i.get_deadline()
        data['todo'].append({'task': task, 'desc': desc, 'time': str(time)})
    json_string = json.dumps(data)
    fernet = Fernet(get_key())
    encrypted_string = fernet.encrypt(json_string.encode())
    with open('dump.dat', 'wb') as f:
        f.write(encrypted_string)


def get_data() -> TodoList:
    encrypted_string = ''
    t = TodoList()
    if not (DATA_FILE in os.listdir('.')):
        return t

    with open('dump.dat', 'rb') as f:
        encrypted_string = f.read()
    fernet = Fernet(get_key())
    json_string = fernet.decrypt(encrypted_string).decode()
    data = json.loads(json_string)
    for i in data['todo']:
        dt = datetime.datetime.strptime(i['time'], "%Y-%m-%d %H:%M:%S.%f")
        t.add_todo(i['task'], i['desc'], dt)
    return t
