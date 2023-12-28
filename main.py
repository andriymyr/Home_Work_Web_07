import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError

from database.repository import create_, update_, remove_, get_all_
from seed import fill_data

parser = argparse.ArgumentParser(description="APP")
parser.add_argument(
    "--action", help="Command: insert_data, create, update, list, remove"
)
parser.add_argument("--id")
parser.add_argument("--name")
parser.add_argument("--id_")
parser.add_argument("--model")

arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get("action")
model = my_arg.get("model")
name = my_arg.get("name")
id_ = my_arg.get("id_")
_id = my_arg.get("id")


def main():
    match action:
        case "insert_data":
            fill_data()
        case "create":
            create_(model, name, id)
        case "list":
            result = get_all_(model)
            for t in result:
                print("--------------------", t)
                # print(t.id, t.name, t.description, t.user.login)
        case "update":
            t = update_(model, _id, name, id_)
            print("--------------------", t)
            # print(t.id, t.title, t.description, t.user.login)
        case "remove":
            r = remove_(_id=_id, user=user)
            print(f"Result: {bool(r)}")


if __name__ == "__main__":
    main()
    sys.exit()
