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
    parser_add.add_argument('title', type=str,
            help='The title of the task - '
                'enclose in quotes if more than one word')
    parser_add.add_argument('description', type=str,
            help='The description of the task - '
                'enclose in quotes if more than one word')
    parser_add.add_argument('deadline', type=float, nargs='?',
            help='Optional argument that sets a deadline for the todo item '
                'in minutes - decimal values are valid')

    parser_add = subparsers.add_parser('view',
            help='View the todo list')
    parser_add.add_argument('view', type=str, default='all', nargs='?',
            help='Displays all todo list items')

    return parser.parse_args(shlex.split(command))


if __name__ == "__main__":

    t= TodoList()
    # multithreading used here st it doesn't interfere with Future to-do Insertion
    t1 = threading.Thread(target=checker, args=(t,), name='t1')
    # this makes the thread auto close when the parent thread closes
    t1.setDaemon(True)
    t1.start()

    while True:
        command = input("\nEnter Command ('--help' for usage instructions "
                "or 'exit' to close) : ").lower() or '--help'
        print()

        if command == "exit":
            exit()

        try:
            parsed = parse_command(command)
        except SystemExit:
            continue

        if parsed.command == 'add':
            if parsed.deadline:
                t.add_todo(parsed.title, parsed.description, parsed.deadline)
            else:
                t.add_todo(parsed.title, parsed.description)
            print(f"\nAdded the todo list item: {parsed.title}\n")

        elif parsed.command == 'view':
            if parsed.view == 'all':
                for task in t.data:
                    print(task)
