from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    serialize_rules = ('-enrolments.student',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    degree = db.Column(db.String)

    enrolments = db.relationship('Enrolment', back_populates='student', cascade='all, delete-orphan')
    courses = association_proxy('enrolments', 'course', creator=lambda c: Enrolment(course=c))

    def __repr__(self):
        return f"<Student {self.id}: {self.name} - {self.degree}>"

class Course(db.Model, SerializerMixin):
    __tablename__ = "classes"

    serialize_rules = ('-enrolments.course',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    enrolments = db.relationship('Enrolment', back_populates='course', cascade='all,delete-orphan')
    students = association_proxy('enrolments', 'student', creator=lambda s: Enrolment(student=s))

    def __repr__(self):
        return f"<Course {self.id}: {self.title}>"

class Enrolment(db.Model, SerializerMixin):
    __tablename__ = "enrolments"

    serialize_rules = ('-student.enrolments', '-course.enrolments')

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    student = db.relationship('Student', back_populates='enrolments')
    course = db.relationship('Course', back_populates='enrolments')

    def __repr__(self):
        return f"<Student {self.id} is enrolled in Class {self.id}>"