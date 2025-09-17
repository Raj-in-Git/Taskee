from app import db

# Model 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    
    def __repr__(self):
        return f'<User {self.name}>'




# to add data @start of script
# with app.app_context():
#     if not User.query.filter_by(email="alice@example.com").first():
#         new_user = User(name="Alice", email="alice@example.com")
#         db.session.add(new_user)
#         db.session.commit()
#         print("✅ User added!")

# with app.app_context():
#     users = User.query.all()
#     print(users)  # will print [<User Alice>] etc.