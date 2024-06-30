from flask_restful import Resource
from models import db, Student, Course, Enrolment
from flask import make_response, request

class Students(Resource):
    # GET /students
    def get(self):
        students = [ student.to_dict() for student in Student.query.all() ]

        return make_response( students, 200)

    # POST /students
    def post(self):
        new_student = Student(name=request.json['name'], degree=request.json['degree'])

        db.session.add(new_student)
        db.session.commit()

        if new_student.id:
            return make_response(new_student.to_dict(), 201)

        return make_response({"error": "Create unsuccessful"}, 403)

class StudentById(Resource):
    # /students/<int:id> - GET, UPDATE, DELETE

    @classmethod
    def find_student(cls, id):
        return Student.query.filter(Student.id == id).first()

    def get(self, id):
        student = StudentById.find_student(id)

        if student:
            return make_response(student.to_dict(), 200)

        return make_response({"error": "No student found"}, 404)

    def patch(self, id):
        student = find_student(id)

        if student:
            for attr in request.json:
                setattr(student, attr, request.json[attr])

            db.session.commit()

            return make_response(student.to_dict(), 200)

        make_response({"error": "No student found"}, 404)

    def delete(self, id):
        student = Student.query.filter(Student.id == id).first()

        if student:
            db.session.delete(student)

            db.session.commit()

            return make_response({"message": "Delete successful"}, 200)

        make_response({"error": "No student found"}, 404)

class StudentEnrol(Resource):
    # POST /students/<int:id>/enrol

    def post(self, id):
        student = Student.query.filter(Student.id == id).first()

        if student:
            course = Course.query.filter(Course.id == request.json['course_id']).first()

            if course:
                # Frae is enrolled in IT 101 (student: 1, course: 1)
                enrolment = Enrolment(course_id=course.id, student_id=student.id)

                db.session.add(enrolment)
                db.session.commit()

                return make_response({"message": "Successfully enrolled!"}, 200)

            return make_response({"error": "No course found"}, 404)

        return make_response({"error": "No student found"}, 404)