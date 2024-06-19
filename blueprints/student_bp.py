from flask import Blueprint, request, jsonify, make_response
from models import db, Student, Enrolment, Class

student_bp = Blueprint('student', __name__, url_prefix="/students")

# Routes
# GET    / - Return all students
# POST   / - Create a new student
# GET    /:student_id - Return student with student_id
# PATCH  /:student_id - Update the student with student_id
# DELETE /:student_id - Delete student with student_id
# POST   /:student_id/enrol - Enrol this student to a class