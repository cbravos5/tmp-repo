import os
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date  # Settings as shown in docker-compose.yml
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5433/postgres')
Session = sessionmaker(bind=engine)
Base = declarative_base()
# from base import Base


class Ala(Base):
    __tablename__ = 'alas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    setores = relationship("Setor", back_populates="ala")

    def __init__(self, nome):
        self.nome = nome


class Setor(Base):
    __tablename__ = 'setores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    ala_id = Column(Integer, ForeignKey('alas.id'))
    ala = relationship("Ala", back_populates="setores")

    def __init__(self, nome):
        self.nome = nome


# class Stuntman(Base):
#     __tablename__ = 'stuntmen'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     active = Column(Boolean)
#     actor_id = Column(Integer, ForeignKey('actors.id'))
#     actor = relationship("Actor", backref=backref("stuntman", uselist=False))

#     def __init__(self, name, active, actor):
#         self.name = name
#         self.active = active
#         self.actor = actor


# class ContactDetails(Base):
#     __tablename__ = 'contact_details'

#     id = Column(Integer, primary_key=True)
#     phone_number = Column(String)
#     address = Column(String)
#     actor_id = Column(Integer, ForeignKey('actors.id'))
#     actor = relationship("Actor", backref="contact_details")

#     def __init__(self, phone_number, address, actor):
#         self.phone_number = phone_number
#         self.address = address
#         self.actor = actor

if(os.environ.get('ENV') == 'commit'):
    Base.metadata.create_all(engine)
    print('Tables created successfully')


session = Session()
