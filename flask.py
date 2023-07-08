from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Titanic.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Passengers(db.Model):
    PassengerId = db.Column(db.Integer, primary_key=True)
    Survived = db.Column(db.Integer)
    Pclass = db.Column(db.Integer)
    Name = db.Column(db.String)
    Sex = db.Column(db.String)
    Age = db.Column(db.Integer)
    Embarked = db.Column(db.String)
    Fare = db.Column(db.Float)


@app.route('/', methods=['GET', 'POST'])
def search_passengers():
    if request.method == 'POST':
        search_input = request.form.get('search_input')
        passengers = []
        if search_input.isdigit():
            passengers = Passengers.query.filter(Passengers.Age == int(search_input)).all()
        else:
            passengers = Passengers.query.filter(Passengers.Sex.ilike(search_input.capitalize())).all()
        return render_template('results.html', passengers=passengers, search_input=search_input)
    return render_template('index.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
