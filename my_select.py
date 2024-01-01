from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from database.db import session
from database.models import Student, Teacher, Grade, Group, Discipline


def select_1(**kwargs):
    print("*" * 60)
    top_students_query = (
        session.query(Student.fullname, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
    )
    for student in top_students_query:
        print(f"Student: {student.fullname}, Average Grade: {student.average_grade}")


def select_2(**kwargs):
    subject_name = kwargs["name"]
    print("+" * 60, subject_name)
    if not subject_name:
        return
    query = (
        session.query(Student.fullname, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Grade.student_id == Student.id)
        .join(Discipline, Discipline.id == Grade.discipline_id)
        .filter(Discipline.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
    )
    top_student = query.first()
    if top_student:
        print(
            f"Top Student for {subject_name}: {top_student.fullname}, Average Grade: {top_student.average_grade}"
        )
    else:
        print(f"No data found for {subject_name}")


def select_3(**kwargs):
    subject_name = kwargs["name"]
    query = (
        session.query(Group.name, func.avg(Grade.grade).label("average_grade"))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Discipline, Discipline.id == Grade.discipline_id)
        .filter(Discipline.name == subject_name)
        .group_by(Group.id)
    )
    for group in query:
        print(f"Group: {group.name}, Average Grade: {group.average_grade}")


def select_4(**kwargs):
    query = (
        session.query(func.avg(Grade.grade).label("average_grade"))
        .join(Student, Student.id == Grade.student_id)
        .join(Discipline, Discipline.id == Grade.discipline_id)
    )

    average_grade = query.scalar()
    if average_grade is not None:
        print(f"Average Grade across all students : {average_grade}")


def select_5(**kwargs):
    teacher_name = kwargs["name"]
    query = (
        session.query(Discipline.name)
        .join(Teacher, Teacher.id == Discipline.teacher_id)
        .filter(Teacher.fullname == teacher_name)
    )

    courses = query.all()
    if courses:
        print(f"Courses taught by {teacher_name}:")
        for course in courses:
            print(course.name)
    else:
        print(f"No courses found for {teacher_name}")


def select_6(**kwargs):
    group_name = kwargs["name"]
    query = (
        session.query(Student.fullname)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
    )

    students = query.all()
    if students:
        print(f"Students in group {group_name}:")
        for student in students:
            print(student.fullname)
    else:
        print(f"No students found in group {group_name}")


def select_7(**kwargs):
    group_name = kwargs["model"]
    subject_name = kwargs["name"]

    query = (
        session.query(Student.fullname, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Discipline, Discipline.id == Grade.discipline_id)
        .filter(Group.name == group_name, Discipline.name == subject_name)
    )

    grades = query.all()
    if grades:
        print(f"Grades in {subject_name} for group {group_name}:")
        for student, grade in grades:
            print(f"Student: {student}, Grade: {grade}")
    else:
        print(f"No grades found for {subject_name} in group {group_name}")


def select_8(**kwargs):
    teacher_name = kwargs["name"]
    query = (
        session.query(func.avg(Grade.grade).label("average_grade"))
        .join(Discipline, Discipline.id == Grade.discipline_id)
        .join(Teacher, Teacher.id == Discipline.teacher_id)
        .filter(Teacher.fullname == teacher_name)
    )

    average_grade = query.scalar()
    if average_grade is not None:
        print(f"Average Grade given by {teacher_name}: {average_grade}")
    else:
        print(f"No data found for {teacher_name}")


def select_9(**kwargs):
    student_name = kwargs["name"]
    query = (
        session.query(Discipline.name)
        .join(Grade, Grade.discipline_id == Discipline.id)
        .join(Student, Student.id == Grade.student_id)
        .filter(Student.fullname == student_name)
    )

    courses = query.all()
    if courses:
        print(f"Courses taken by {student_name}:")
        for course in courses:
            print(course.name)
    else:
        print(f"No courses found for {student_name}")


def select_10(**kwargs):
    student_name = kwargs["model"]
    teacher_name = kwargs["name"]
    query = (
        session.query(Discipline.name)
        .join(Teacher, Teacher.id == Discipline.teacher_id)
        .join(Grade, Grade.discipline_id == Discipline.id)
        .join(Student, Student.id == Grade.student_id)
        .filter(Teacher.fullname == teacher_name, Student.fullname == student_name)
    ).distinct()

    courses = query.all()
    if courses:
        print(f"Courses taught by {teacher_name} to {student_name}:")
        for course in courses:
            print(course.name)
    else:
        print(f"No courses found for {teacher_name} to {student_name}")


def selects(number=None, name=None, id=None, model=None):
    if not number:
        return
    func_name = f"select_{number}"
    if func_name in globals():
        function_to_call = globals()[func_name]
        function_to_call(name=name, id=id, model=model)
