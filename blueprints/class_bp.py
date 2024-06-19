from flask import Blueprint, request, jsonify, make_response
from models import db, Student, Enrolment, Class

class_bp = Blueprint('class', __name__, url_prefix="/classes")

# Routes
# GET    / - Return all classes
# POST   / - Create a new class
# GET    /:class_id - Return class with class_id
# PATCH  /:class_id - Update the class with class_id
# DELETE /:class_id - Delete class with class_id
# GET    /:class_id/students - Return all students from the class with class_id