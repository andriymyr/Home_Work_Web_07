import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
#from database.repository import get_user, get_all_todos, create_todo, update_todo, remove_todo
import database.repository 

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')
title = my_arg.get('title')
description = my_arg.get('desc')
_id = my_arg.get('id')
login = my_arg.get('login')


def main():
    match action:
        case 'create':
            create_todo(title=title, description=description, user=user)
        case 'list':
            todos = get_all_todos(user)
            for t in todos:
                print(t.id, t.title, t.description, t.user.login)
        case 'update':
            t = update_todo(_id=_id, title=title, description=description, user=user)
            print(t.id, t.title, t.description, t.user.login)
        case 'remove':
            r = remove_todo(_id=_id, user=user)
            print(f'Result: {bool(r)}')


if __name__ == '__main__':

    main()
    sys.exit()
