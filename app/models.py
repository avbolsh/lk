from app.extension import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
import uuid
from . import login



class User(UserMixin, db.Model):
    id = Column(Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    surname = Column(String(64))
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    last_seen = Column(DateTime, default=datetime.utcnow)
    inn = Column(String(length=12))
    snils = Column(String(length=11))


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
