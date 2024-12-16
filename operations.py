"""Operations with database module"""

from sqlalchemy.orm import sessionmaker

from model_and_connect import engine, User, Post

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# Add multiple rows in Users

""" db.add(User(username="Jack", email="Jackie@mail.com", password="easyashell"))
db.add(User(username="John", email="Johnie@mail.com", password="hardasnutcrack456&*("))
db.commit() """

# Add multiple rows in Posts, connected to Users

db.add(Post(title="New news!", content="Today morning, nothing happened!", user_id="1"))
db.add(Post(title="Old news", content="Today morning, nothing happened!", user_id="2"))
db.commit()

# Get and display all Users data

users = db.query(User).all()
for u in users:
    print(f"{u.id}: {u.username} {u.email}")
