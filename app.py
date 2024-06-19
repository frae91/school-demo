from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db
from blueprints.course_bp import course_bp
from blueprints.student_bp import student_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///school.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.register_blueprint(course_bp)
app.register_blueprint(student_bp)

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return make_response( jsonify( { "message": "Welcome to the School App!" } ), 200)

if __name__ == "__main__":
    app.run(port=4000, debug=True)