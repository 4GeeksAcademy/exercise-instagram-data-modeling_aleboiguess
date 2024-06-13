import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    address = relationship("Address" , back_populates="address")
    post = relationship("Post" , back_populates="post")
    post_comments = relationship("Post_Comments" , back_populates="post_comments")


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    
    def to_dict(self):
        return {}
    
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    created_at = Column(String(250))
    post_comments = relationship("Post_Comments" , back_populates="post_comments")


class Post_Comments(Base):
    __tablename__ = "post_comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    person_id = Column(Integer, ForeignKey("person.id"))



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
