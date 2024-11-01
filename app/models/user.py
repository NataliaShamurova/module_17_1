from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    slug = Column(String, unique=True, index=True)

    # from app.models import Task
    tasks = relationship('Task', back_populates='user')


print(CreateTable(User.__table__))
