from module_17_1.app.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


# from module_17_1.app.backend.db import Base
# from module_17_1.app.models.user import User
# from module_17_1.app.models.task import Task
# target_metadata = Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

