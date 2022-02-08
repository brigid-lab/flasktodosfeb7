from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///"

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    task = db.Column(db.String(30), nullable=False)
    completed =db.Column(db.Boolean, default =False)


# create sample task-good for testing
#test the table can accept the entry and there is nothing wrong with the code
db.create_all()
sample_todo = Todos(
    task = "Teaching Flask -testing drop all command",
    completed =False
)

#the task to the table adding 
db.session.add (sample_todo)
db.session.commit()

#link to website look for what we have tried to enter
@app.route('/')
def index():
    todo = Todos.query.first()
    return todo.task

@app.route('/add')
def add():
    return "Add a new Todo"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


