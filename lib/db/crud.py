from models import Organizer, Venue, Participant, MentorshipSession, session
#CRUD OPERATIONS on Organizer
#CREATE
#Adding organizers
def add_organizer(first_name, last_name, email_address, phone_number):
    new_organizer = Organizer(first_name = first_name, last_name = last_name, email_address = email_address, phone_number = phone_number)
    session.add(new_organizer) #updates the changes in the database
    session.commit() #saves the changes permanently in the database

add_organizer(first_name="Ianni", 
              last_name="Bona", 
              email_address="iannibona@gmail.com", 
              phone_number=5689012
)
organizers = session.query(Organizer).all()
for organizer in organizers:
    print(f"{organizer.first_name} {organizer.last_name}")



#Adding participant
def add_participant(first_name, last_name, email_address, phone_number, venue_id):
    new_participant = Participant(first_name = first_name, last_name = last_name, email_address = email_address, phone_number = phone_number, venue_id = venue_id)
    session.add(new_participant)
    session.commit()

#Adding venues
def add_venue(name, location, capacity):
    new_venue = Venue(name = name, location = location, capacity = capacity)
    session.add(new_venue)
    session.commit()

#adding mentorship sessions
def add_mentorship_session(title, date, description, organizer_id, venue_id):
    new_mentorship_session = MentorshipSession(title = title, date = date, description = description, organizer_id = organizer_id, venue_id = venue_id)
    session.add(new_mentorship_session)
    session.commit()

#READ
#retrieve all organizers
def get_organizers():
    organizers = session.query(Organizer).all()
    return organizers
#These commented lines were for testing
"""organizers = get_organizers()
for organizer in organizers:
    print(f"ID: {organizer.id}, First name: {organizer.first_name}, Last name: {organizer.last_name}")
"""

#retrieve all participants
def get_participants():
    participants = session.query(Participant).all()
    return participants
"""participants = get_participants()
for participant in participants:
    print(f"ID: {participant.id}, First name: {participant.first_name}, Last name: {participant.last_name}")
"""

#retriebe all venues
def get_venues():
    venues = session.query(Venue).all()
    return venues
"""venues = get_venues()
for venue in venues:
    print(f"ID: {venue.id}, Name: {venue.name}, Location: {venue.location}, Capacity: {venue.capacity}")
"""

#retrieve mentorship sessions
def get_mentorship_sessions():
    mentorship_sessions = session.query(MentorshipSession).all()
    return mentorship_sessions

"""mentorship_sessions = get_mentorship_sessions()
for mentorship_session in mentorship_sessions:
    print(f"ID: {mentorship_session.id}, title: {mentorship_session.title}")
"""


#Updating functions
#updating organizers
def update_organizer(organizer_id, first_name = None, last_name = None, email_address = None, phone_number = None):
    #find the organizer by id
    organizer = session.query(Organizer).filter_by(id=organizer_id).first()
    if organizer: #if found
        if first_name is not None:
            organizer.first_name = first_name
        if last_name is not None:
            organizer.last_name = last_name
        if email_address is not None:
            organizer.email_address = email_address
        if phone_number is not None:
            organizer.phone_number = phone_number
        session.commit()
        print(f"Organizer ID {organizer_id} is updated successfully")
    else:
        print(f"There is no organizer with ID:{organizer_id}")


#updating participants
def update_participant(participant_id, first_name, last_name, email_address, phone_number):
    participant = session.query(Participant).filter_by(id=participant_id).first()
    #DONT FORGET .first() to return the first result. YOU KEEP FORGETING
    if participant:
        if first_name is not None:
            participant.first_name = first_name
        if last_name is not None:
            participant.last_name = last_name
        if email_address is not None:
            participant.email_address = email_address
        if phone_number is not None:
            participant.phone_number = phone_number
        session.commit()
        print(f"Participant ID {participant_id} is updated successfully")
    else:
        print(f"There is no participant with ID:{participant_id}")

#updating venues
def update_venue(venue_id, name = None, location = None, capacity=None):
    venue = session.query(Venue).filter_by(id=venue_id).first()
    if venue:
        if name is not None:
            venue.name = name
        if location is not None:
            venue.location = location
        if capacity is not None:
            venue.capacity = capacity

        session.commit()
        print(f"Venue  ID {venue_id} is updated successfully")
    else:
        print(f"There is no venue with ID:{venue_id}")

#updating mentorship sessions
def update_mentorship_session(mentorship_session_id, title, date=None, description=None):
    mentorship_session = session.query(MentorshipSession).filter_by(id=mentorship_session_id).first()
    if mentorship_session:
        if title is not None:
            mentorship_session.title = title
        if date is not None:
            mentorship_session.date = date
        if description is not None:
            mentorship_session.desciption = description
        
        session.commit()
        print(f"Mentorship session  ID {mentorship_session_id} is updated successfully")
    else:
        print(f"There is no mentorship session with ID:{mentorship_session_id}")

update_organizer(1, first_name="Cheryl", email_address="newmail@example.com")
update_mentorship_session(2, title="Leadership & Growth", date = "2025-09-25", description="Session on Leadership and Growth")
update_participant(3, first_name="John", last_name="Doe", email_address="johndoe@gmail.com", phone_number=8899776655)
update_venue(3, name="Nairobi Hub", location="Westlands")


#DELETE
