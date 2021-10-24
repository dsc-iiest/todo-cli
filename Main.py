import datetime

from modules.TodoList import TodoList
from modules.TodoListChecker import checker
from modules.saveTodos import *

import argparse
import threading
import shlex
import os

def parse_command(command: str):
    """
    Parses a command and returns Namespace of the results.

    Parameters:
    command (str): The command to parse

    Returns:
    Namespace object - comprised of values relevant to the command parameter
    """
    parser = argparse.ArgumentParser(
            description='Full Fledged Command Line Based Todo List')
    subparsers = parser.add_subparsers(dest='command',
            help='Available todo list commands')

    parser_add = subparsers.add_parser('add',
            help='Add a new task to the todo list')
    parser_add.add_argument('title', type=str,
            help='The title of the task - '
                'enclose in quotes if more than one word')
    parser_add.add_argument('description', type=str,
            help='The description of the task - '
                'enclose in quotes if more than one word')
    parser_add.add_argument('--time', type=str, nargs='?',
            help='Optional argument that sets a deadline for the todo item - '
                'deadline should be given in format dd/mm/YYYY H:M enclosed in quotes.'
                'Time should be given in 24 hours format')
    parser_add.add_argument('--offset', type=float, nargs='?', default=1,
            help='Optional argument that sets a deadline for the todo item '
                 'in minutes - decimal values are valid.'
                 'By default, each todo item will have a minute deadline.')

    parser_add = subparsers.add_parser('view',
            help='View the todo list')
    parser_add.add_argument('view', type=str, default='all', nargs='?',
            help='Displays all todo list items')

    return parser.parse_args(shlex.split(command))


def get_notification_datetime_from_time_or_offset(notification_time_str: str = None, offset: int = None):
    try:
        if notification_time_str:
            notification_time = datetime.datetime.strptime(notification_time_str, "%d/%m/%Y %H:%M")
            if notification_time <= datetime.datetime.now():
                raise ValueError
        else:
            notification_time = datetime.datetime.now() + datetime.timedelta(minutes=offset)
        return notification_time
    except ValueError:
        print("Notification time provided is either in wrong format or invalid.")
        return None


if __name__ == "__main__":

    t= getData()
    # multithreading used here st it doesn't interfere with Future to-do Insertion
    t1 = threading.Thread(target=checker, args=(t,), name='t1')
    # this makes the thread auto close when the parent thread closes
    t1.setDaemon(True)
    t1.start()

    while True:
        command = input("\nEnter Command below ('--help' for usage "
                "instructions or 'exit' to close):\n").lower() or '--help'

        if command == "exit":
            saveData(t)
            exit()

        try:
            parsed = parse_command(command)
        except SystemExit:
            continue

        if parsed.command == 'add':
            notification_datetime = get_notification_datetime_from_time_or_offset(parsed.time, parsed.offset)
            if notification_datetime:
                t.add_todo(parsed.title, parsed.description, notification_datetime)
                print(f"\nAdded the todo list item: {parsed.title}")
            else:
                print(f"\nCannot add the todo list item: {parsed.title}")
                continue

        elif parsed.command == 'view':
            if parsed.view == 'all':
                if t.data:
                    for task in t.data:
                        print(task)
                else:
                    print("\nTodo list is empty - add some items with the "
                            "'add' command")
