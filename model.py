from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :



from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here
class Donation(Base):
	__tablename__="donations"
	donation_id=Column(Integer,primary_key=True)
	donor_id = Column(Integer, ForeignKey('donors.donor_id'))
	name=Column(String)
	amount=Column(Integer)
	expiration_date=Column(String)
	donor = relationship("Donor", back_populates = "donation")

class Donor(Base):
	__tablename__="donors"
	donor_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	area=Column(String)
	address=Column(String)
	telephone=Column(String)
	donation = relationship("Donation", back_populates = "donor")

class Reciever(Base):
	__tablename__ = "recievers"
	reciever_id = Column(Integer, primary_key = True)
	reciever_name = Column(String)
	email = Column(String)
	password = Column(String)
	area = Column(String)
	telephone = Column(String)
	request = relationship("Request", back_populates = "reciever")

class Request(Base):
	__tablename__="requests"
	request_id=Column(Integer,primary_key=True)
	reciever_id = Column(Integer, ForeignKey('recievers.reciever_id'))
	name=Column(String)
	amount=Column(Integer)
	reciever = relationship("Reciever", back_populates = "request")

