from app.extension import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(64))
    last_name = Column(String(64))
    surname = Column(String(64))
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    last_seen = Column(DateTime, default=datetime.utcnow)