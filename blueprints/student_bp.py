from flask import Blueprint, request, jsonify, make_response
from models import db, Student, Enrolment, Course

student_bp = Blueprint('student', __name__, url_prefix="/students")

# Routes
# GET    / - Return all students
# POST   / - Create a new student
@student_bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        students_from_db = Student.query.all()

        students = []
        for student in students_from_db:
            students.append(student.to_dict())

        return make_response(jsonify(students), 200)
    elif request.method == "POST":
        new_student = Student(name=request.json['name'], degree=request.json['degree'])
        db.session.add(new_student)
        db.session.commit()

        if new_student.id:
            return make_response( jsonify(new_student.to_dict()), 201)

        return make_response( jsonify({"error": "Error"}), 403)
# GET    /:student_id - Return student with student_id
# PATCH  /:student_id - Update the student with student_id
# DELETE /:student_id - Delete student with student_id
@student_bp.route('/<int:student_id>', methods=['GET', 'PATCH', "DELETE"])
def get_student(student_id):
    student = Student.query.filter(Student.id == student_id).first()

    if student:
        if request.method == "GET":
            return make_response(jsonify(student.to_dict()), 200)
        elif request.method == "PATCH":
            for attr in request.json:
                setattr(student, attr, request.json[attr])

            db.session.commit()

            return make_response(jsonify(student.to_dict()), 200)
        elif request.method == "DELETE":
            db.session.delete(student)
            db.session.commit()

            return make_response(jsonify({"message": "Successfully deleted"}), 200)


    return make_response(jsonify({"error": "Student not found"}), 403)
# POST   /:student_id/enrol - Enrol this student to a class
@student_bp.route('/<int:student_id>/enrol', methods=['POST'])
def enrol(student_id):
    student = Student.query.filter(Student.id == student_id).first()

    if student:
        course = Course.query.filter(Course.id == request.json['course_id']).first()

        if course:
            new_enrolment = Enrolment(student_id=student.id, course_id=course.id)
            db.session.add(new_enrolment)
            db.session.commit()

            return make_response(jsonify({"message": f"{student.name} is successfully enrolled in {course.title}!"}), 200)

        return make_response(jsonify({"error": "Course is not found"}), 404)

    return make_response(jsonify({"error": "Student not found"}), 403)
