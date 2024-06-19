# School Demo (Flask)

- This is a starter code for a Flask application.

---

## Setup

Run ```pipenv install``` and ```pipenv shell```

### Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy-Serializer

### Models & Relationships

- ```Student```, ```Class```, ```Enrolment```
- ```Student``` has many ```Class```es, through ```Enrolment```s
- ```Class``` has many ```Student```s, through ```Enrolment```s
- ```Enrolment``` belongs to a ```Student```, ```Enrolment``` belongs to a ```Class```