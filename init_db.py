from app import db, app
from models import User

# Create tables
with app.app_context():
    db.create_all()