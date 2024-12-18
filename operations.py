"""Operations with database module"""

from database import Base, engine, SessionLocal, User, Post

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Add multiple rows in Users

if db.query(User).filter(User.username == "Jack").first() is None:
    db.add(User(username="Jack", email="Jackie@mail.com", password="easyashell"))

if db.query(User).filter(User.username == "John").first() is None:
    db.add(
        User(username="John", email="Johnie@mail.com", password="hardasnutcrack456&*(")
    )
db.commit()

# Add multiple rows in Posts, connected to Users

jack = db.query(User).filter(User.username == "Jack").first()
john = db.query(User).filter(User.username == "John").first()
db.add(
    Post(title="New news!", content="Today morning, nothing happened!", user_id=jack.id)
)
db.add(
    Post(title="Old news", content="Today morning, nothing happened!", user_id=john.id)
)
db.add(
    Post(
        title="Old old news",
        content="It's morning and as usually in the last 20 years, nothing happened!",
        user_id=john.id,
    )
)
db.commit()

# Get and display all Users data

print("Users:")
users = db.query(User).all()
for u in users:
    print(f"{u.id}: {u.username} {u.email}")

# Get one User's all Posts

print("\nPosts:")
posts = db.query(Post).filter(Post.user_id == jack.id).all()
for p in posts:
    print(f"{p.title}: {p.content}")

# Edit one User's email

print("\nEditing Jack's email:")
print(jack.email)
if jack.email == "memi@mail.ru":
    jack.email = "mamumu@mail.ur"
else:
    jack.email = "memi@mail.ru"
db.commit()

print(db.query(User).filter(User.username == "Jack").first().email)

# Edit one Post's content

print("\nEditing Jack's first post content:")
post = db.query(Post).filter(Post.id == 1).first()
print(post.content)
if post.content == "Propaganda":
    post.content = "Sunny day today!"
else:
    post.content = "Propaganda"
db.commit()

print(db.query(Post).filter(Post.id == 1).first().content)

# Deleting John's post
db.delete(db.query(Post).filter(Post.user_id == john.id).first())
db.commit()

# Deleting John and his posts

posts = db.query(Post).filter(Post.user_id == john.id).all()
for p in posts:
    db.delete(p)
db.commit()
db.delete(john)
db.commit()
