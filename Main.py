from modules.TodoList import TodoList
from modules.TodoListChecker import checker

import argparse
import threading
import shlex


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
    parser_add.add_argument('title', type=str, help='The title of the task')
    parser_add.add_argument('description', type=str,
            help='The description of the task')
    parser_add.add_argument('deadline', type=float, nargs='?',
            help='An optional deadline argument in minutes')

    parser_add = subparsers.add_parser('view',
            help='View the todo list')
    parser_add.add_argument('view', type=str, choices=('all', 'overdue'),
            default='all', nargs='?',
            help='What type of view you want to invoke')

    return parser.parse_args(shlex.split(command))


if __name__ == "__main__":

    while True:
        command = input("\nEnter Command ('--help' for usage instructions "
                "commands or 'exit' to close) : ").lower()

        if command == "exit":
            exit()

        try:
            parsed = parse_command(command)
        except SystemExit:
            continue

        t= TodoList()

        if parsed.command == 'add':
            t.add_todo(parsed.title, parsed.description, parsed.deadline)
            print("\nTask added\n")

        elif parsed.command == 'view':
            # View command logic will go here with
            # parsed.view will be the keyword for options like 'all', 'overdue'
            print("To-do list will be printed to screen here")
            pass

        else:
            exit()

        t.add_todo(
            task='Wash Dishes',
            description="Don't forget to use Vim bar also",
            minute_deadline_offset=1.5)

        t.add_todo(
            task='Hang Clothes',
            description="Also install new hanging rope",
            minute_deadline_offset=0.5)

        t.add_todo(
            task='Run Washing Machine',
            description="Also use Comfort in the end",
            minute_deadline_offset=1)

        # multithreading used here st it doesn't interfere with Future to-do Insertion
        t1 = threading.Thread(target=checker, args=(t,), name='t1')
        # this makes the thread auto close when the parent thread closes
        t1.setDaemon(True)
        t1.start()
