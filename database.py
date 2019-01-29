from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass
    


def add_donor(name, email, password, telephone):
	donor_object = Donor(
		name=name,
		email = email,
		password = password,
		telephone=telephone)
	session.add(donor_object)
	session.commit()





def query_donors_by_email(email):
	donor = session.query(Donor).filter_by(email=email).first()
	return donor



def query_recievers_by_email(email):
	reciever = session.query(Reciever).filter_by(email=email).first()
	return reciever



	