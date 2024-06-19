from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    degree = db.Column(db.String)

    def __repr__(self):
        return f"<Student {self.id}: {self.name} - {self.degree}>"

class Class(db.Model, SerializerMixin):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Class {self.id}: {self.title}>"

class Enrolment(db.Model, SerializerMixin):
    __tablename__ = "enrolments"

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return f"<Student {self.id} is enrolled in Class {self.id}>"