import argparse
import sys
import my_select
from sqlalchemy.exc import SQLAlchemyError


from database.repository import create_, update_, remove_, get_all_
from seed import fill_data

parser = argparse.ArgumentParser(description="APP")
parser.add_argument(
    "--action", help="Command: insert_data, create, update, list, remove, select"
)
parser.add_argument("--id")
parser.add_argument("--name")
parser.add_argument("--id_")
parser.add_argument("--model")
parser.add_argument("--number")

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get("action")
model = my_arg.get("model")
name = my_arg.get("name")
id_ = my_arg.get("id_")
_id = my_arg.get("id")
number = my_arg.get("number")


def main():
    match action:
        case "insert_data":
            fill_data()
        case "create":
            create_(model, name, id_)
        case "list":
            result = get_all_(model)
            for t in result:
                if model == "Teacher":
                    print(t.id, " ", t.fullname)
                elif model == "Student":
                    print(t.id, " ", t.fullname, t.group_id)
                elif model == "Group":
                    print(t.id, " ", t.name)
        case "update":
            t = update_(model, _id, name, id_)
            if model == "Teacher":
                print(t.id, " ", t.fullname)
            elif model == "Student":
                print(t.id, " ", t.fullname, t.group_id)
            elif model == "Group":
                print(t.id, " ", t.name)
        case "remove":
            r = remove_(model, _id=_id)
            print(f"Result: {bool(r)}")
        case "select":
            my_select.selects(number, name=name, id=id, model=model)


if __name__ == "__main__":
    main()
    sys.exit()


"""
внесення даних в таблиці
py main.py --action insert_data

відображення даних в таблиці
py main.py --action list --model Teacher 
py main.py --action list --model Student
py main.py --action list --model Group 


створення окремого запису
py main.py --action create --model Teacher --name "Test from Test"
py main.py --action create --model Student --name "Testing from Testing" --id_ 2
py main.py --action create --model Group --name "Test Group" 

, , list, 

зміна окремого запису
py main.py --action update --model Teacher --id 4 --name Test
py main.py --action update --model Student --id 4 --name Test --id_ 1
py main.py --action update --model Group --id 4 --name Test


видалення окремого запису
py main.py --action remove --model Teacher --id 5
py main.py --action remove --model Student --id 5
py main.py --action remove --model Group --id 5

виконання запитів
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
py main.py --action select --number 1
    Знайти студента із найвищим середнім балом з певного предмета.
py main.py --action select --number 2 --name "Вища математика"
    Знайти середній бал у групах з певного предмета.
py main.py --action select --number 3 --name "Вища математика"
    Знайти середній бал на потоці (по всій таблиці оцінок).
py main.py --action select --number 4
    Знайти які курси читає певний викладач.
py main.py --action select --number 5 --name "David Wilson"
    Знайти список студентів у певній групі.
py main.py --action select --number 6 --name "СПД2"
    Знайти оцінки студентів у окремій групі з певного предмета.
py main.py --action select --number 7 --name "Системне програмування" --model "СПД2"
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
py main.py --action select --number 8 --name "David Wilson"
    Знайти список курсів, які відвідує певний студент.
py main.py --action select --number 9 --name "Bethany Weaver"
    Список курсів, які певному студенту читає певний викладач.
"""
