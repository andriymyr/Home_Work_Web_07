from sqlalchemy import and_
from .db import session
from .models import Student, Teacher, Group


def create_(model, name, id):
    if model == "Teacher":
        models = Teacher(fullname=name)
    elif model == "Student":
        models = Student(fullname=name, group_id=id)
    elif model == "Group":
        models = Group(name=name)
    else:
        session.close()
        return ""
    session.add(models)
    session.commit()
    session.close()


def get_all_(model):
    if model == "Teacher":
        result = session.query(Teacher).all()
    elif model == "Student":
        result = session.query(Student).all()
    elif model == "Group":
        result = session.query(Group).all()
    else:
        return ""
    return result


def update_(model, _id, name, id_):
    if model == "Teacher":
        result = session.query(Teacher).filter(Teacher.id == _id)
        result.update({"fullname": name})
    elif model == "Student":
        result = session.query(Student).filter(
            and_(Student.id == _id, Student.group_id == id_)
        )
        result.update({"fullname": name, "group_id": id_})
    elif model == "Group":
        result = session.query(Group).filter(Group.id == _id)
        result.update({"name": name})
    else:
        session.close()
        return ""
    session.commit()
    session.close()
    return result.one()


def remove_(model, _id, name, id_):
    if model == "Teacher":
        r = session.query(Teacher).filter(Teacher.id == _id).delete()
    elif model == "Student":
        r = session.query(Student).filter(Student.id == _id).delete()
    elif model == "Group":
        r = session.query(Group).filter(Group.id == _id).delete()
    else:
        session.close()
        return ""
    session.commit()
    session.close()
    return r
