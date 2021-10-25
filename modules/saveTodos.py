import json
from cryptography.fernet import Fernet
import datetime
import os

from .TodoList import TodoList
from .Todo import Todo

key_file = 'key'
data_file = 'dump.dat'

def getKey() :
    if key_file in os.listdir('.') :
        return open('./key', 'rb').read()
    else :
        key = Fernet.generate_key()
        with open('./key', 'wb') as f:
            f.write(key)
        return key
    

def saveData(t: TodoList) :
    data = {}
    data['todo'] = []
    for i in t.data :
        task = i.get_task()
        desc = i.get_desc()
        time = i.get_deadline()
        data['todo'].append({'task': task, 'desc': desc, 'time': str(time)})
    jsonString = json.dumps(data)
    fernet = Fernet(getKey())
    encryptedString = fernet.encrypt(jsonString.encode())
    with open('dump.dat', 'wb') as f :
        f.write(encryptedString)

def getData()-> TodoList :
    encryptedString = ''
    t = TodoList()
    if not (data_file in os.listdir('.')) :
        return t

    with open('dump.dat', 'rb') as f :
        encryptedString = f.read()
    fernet = Fernet(getKey())
    jsonString = fernet.decrypt(encryptedString).decode()
    data = json.loads(jsonString)
    for i in data['todo'] :
        dt = datetime.datetime.strptime(i['time'], "%Y-%m-%d %H:%M:%S.%f")
        t.add_todo(i['task'], i['desc'], dt)
    return t  


    

