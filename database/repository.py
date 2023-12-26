from sqlalchemy import and_
from .db import session




"""
def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()
    session.close()


def get_all_todos(user) -> list[Todo]:
    todos = session.query(Todo).join(User).filter(Todo.user == user).all()
    return todos


def update_todo(_id, title, description, user) -> Todo:
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
    todo.update({'title': title, 'description': description})
    session.commit()
    session.close()
    return todo.one()


def remove_todo(_id, user) -> int:
    r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).delete()
    session.commit()
    session.close()
    return r
"""