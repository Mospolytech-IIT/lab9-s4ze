"""Main module"""

from fastapi import FastAPI, Depends, encoders, Body, Response
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, User

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """Initialization of db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    """Returns index page"""
    return FileResponse("./index.html")


@app.get("/api/users")
def get_users(db: Session = Depends(get_db)):
    """Get users list"""
    users = db.query(User).all()

    return JSONResponse(
        content=list(
            encoders.jsonable_encoder(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            )
            for user in users
        )
    )


@app.post("/api/users")
def create_user(data=Body(), db: Session = Depends(get_db)):
    """Create user"""
    db.add(User(username=data["username"], email=data["email"]))
    db.commit()
    user = db.query(User).filter(User.username == data["username"]).first()

    return JSONResponse(
        content=encoders.jsonable_encoder(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        )
    )


@app.put("/api/users/{id_}")
def edit_user(id_: int, data=Body(), db: Session = Depends(get_db)):
    """Edit user"""
    user = db.query(User).filter(User.id == id_).first()
    user.username = data["username"]
    user.email = data["email"]
    user.password = data["password"]
    db.commit()

    return JSONResponse(
        content=encoders.jsonable_encoder(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        )
    )


@app.delete("/api/users/{id_}")
def remove_user(id_: int, db: Session = Depends(get_db)):
    """Remove user"""
    user = db.query(User).filter(User.id == id_).first()
    try:
        db.delete(user)
        Response(status_code=200)
        db.commit()
    except:
        Response(status_code=400)

    return Response()
