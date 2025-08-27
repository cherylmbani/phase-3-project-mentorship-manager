from models import MentorshipSession, Organizer, Participant, Venue, session
organizer1 = Organizer(first_name="Cheryl", last_name="Mbani",
                       email_address="cheryl@gmail.com", phone_number=123456789)

session.add(organizer1)
session.commit()
#test this if it can be retrieved
organizers = session.query(Organizer).all()
for org in organizers:
    print(org.id, org.first_name, org.last_name, org.email_address, org.phone_number)



participant1 = Participant(first_name = "Loren", last_name = "Spears", email_address = "lorenspears@gmail.com", phone_number = 1458000812)
session.add(participant1)
session.commit()

venue1 = Venue(name = "Nairobi Cinema", location = "Nairobi", capacity = 500)
session.add(venue1)
session.commit()

mentorship_session1 = MentorshipSession(title = "Emotional Intelligence", description = "a guided conversation where a mentor helps mentees develop skills to recognize, manage, and respond to emotions effectively for personal and professional growth.", venue_id = 1, organizer_id = 1)
session.add(mentorship_session1)
session.commit()
