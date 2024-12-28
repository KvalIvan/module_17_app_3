from module_17_1.app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')

# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(Task.__table__))
# При проверке этим кодом вылезает ошибка пока не знаю что делать
# raise exc.NoReferencedTableError(
# sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'tasks.user_id' could not find table 'users' with which to generate a foreign key to target column 'id'
