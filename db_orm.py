from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
	__tablename__ = "person"

	id = Column('id', Integer, primary_key=True)
	username = Column('username', String) 

engine = create_engine('sqlite:///orm.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def add_user(new_id,new_username):
	new_user = User()
	new_user.id = new_id
	new_user.username = new_username
	session.add(new_user)
	session.commit()

def list_users():
	users = session.query(User).all()
	for user in users:
		print(user.username)

session = Session()

add_user(5,'someguy')
list_users()

session.close()