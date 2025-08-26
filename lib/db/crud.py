from models import Organizer, Venue, Participant, Session, session
#CRUD OPERATIONS on Organizer
def add_organizer(first_name, last_name, email_address, phone_number):
    new_organizer = Organizer(first_name = first_name, last_name = last_name, email_address = email_address, phone_number = phone_number)
    session.add(new_organizer) #updates the changes in the database
    session.commit() #saves the changes permanently in the database

def add_participant(first_name, last_name, email_address, phone_number, venue_id):
    new_participant = Participant(first_name = first_name, last_name = last_name, email_address = email_address, phone_number = phone_number, venue_id = venue_id)
    session.add(new_participant)
    session.commit()

def add_venue(name, location, capacity):
    new_venue = Venue(name = name, location = location, capacity = capacity)
    session.add(new_venue)
    session.commit()

def add_session(title, description, organizer_id, venue_id):
    new_session = Session(title = title, description = description, organizer_id = organizer_id, venue_id = venue_id)
    session.add(new_session)
    session.commit()
