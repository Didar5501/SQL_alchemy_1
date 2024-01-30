from sqlalchemy import Table,Column, String, Integer, MetaData, ForeignKey

metadata= MetaData()

students_table= Table(
    'students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
)

courses_table = Table(
    'courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('course_name', String),
    Column('student_id', Integer, ForeignKey('students.id')) 
)

# 2-ой вариант с отдельной таблицей связей - кажется более правильный
courses_table = Table(
    'courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('course_name', String),
)

courses_students_table = Table(
    'courses_students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('student_id', Integer, ForeignKey('students.id'))
)