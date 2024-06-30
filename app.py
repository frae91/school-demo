from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db
from blueprints.course_bp import course_bp
from blueprints.student_bp import student_bp
from flask_restful import Api
from controllers.courses_controller import Courses, CourseById
from controllers.students_controller import Students, StudentById, StudentEnrol

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///school.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# app.register_blueprint(course_bp)
# app.register_blueprint(student_bp)

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

@app.route('/')
def index():
    return make_response( jsonify( { "message": "Welcome to the School App!" } ), 200)

api.add_resource(Courses, '/courses')
api.add_resource(CourseById, '/courses/<int:id>')

api.add_resource(Students, '/students')
api.add_resource(StudentById, '/students/<int:id>')

api.add_resource(StudentEnrol, '/students/<int:id>/enrol')

if __name__ == "__main__":
    app.run(port=4000, debug=True)