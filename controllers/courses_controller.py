from flask_restful import Resource
from models import db, Course
from flask import make_response, request, jsonify

class Courses(Resource):
    # GET /courses
    def get(self):
        courses = [ course.to_dict() for course in Course.query.all() ]

        return make_response( courses, 200 )

    # POST /courses
    def post(self):
        new_course = Course(title=request.json['title'])

        db.session.add(new_course)
        db.session.commit()

        if new_course.id:
            return make_response(new_course.to_dict(), 201)

        return make_response({"error": "Create unsuccessful"}, 403)

class CourseById(Resource):
    # GET /course/<int:id>
    def get(self, id):
        course = Course.query.filter(Course.id == id).first()

        if course:
            return make_response( course.to_dict(), 200 )

        return make_response({"error": "No course found"}, 404)

