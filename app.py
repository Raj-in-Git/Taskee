from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from datetime import datetime, timezone


app = Flask(__name__)

# Database connection
server = r'BAND-C-00164\SQLEXPRESS'
database = 'tracker'
username = 'raj'
password = '#@Raj270598$'

password_encoded = quote_plus(password)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mssql+pyodbc://{username}:{password_encoded}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Model (must be defined before db.create_all) ---
class Tracker(db.Model):
    __tablename__ = 'tracker'
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(100))
    details = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now().replace(microsecond=0))  # date + time
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now().replace(microsecond=0), onupdate=lambda: datetime.now().replace(microsecond=0))
    

    def __repr__(self):
        return f'<User {self.name}>'

# --- Create tables ---
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    tasks = Tracker.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    taskname = request.form['taskname']
    details = request.form['details']
    new_task = Tracker(taskname=taskname, details=details)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    task = Tracker.query.get(id)
    task.taskname = request.form['taskname']
    task.details = request.form['details']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Tracker.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
