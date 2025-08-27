from lib.db.crud import add_mentorship_session, add_organizer, add_participant, add_venue

# we want to populate our database with initial data
#seed mentorship sessions
add_mentorship_session(
    title = "Emotional Intelligence",
    date="2026-01-14",
    description = "a guided conversation where a mentor helps mentees develop skills to recognize, manage, and respond to emotions effectively.", 
    venue_id = 1, 
    organizer_id = 1
)
add_mentorship_session(
    title="Leadership & Growth",
    date="2025-09-09",
    description="Session on developing leadership skills and personal growth.",
    venue_id=2,
    organizer_id=2
)

#Seed organizers
add_organizer(first_name="Cheryl", last_name="Mbani",email_address="cheryl@gmail.com", phone_number=123456789)
add_organizer(first_name="Gianna", last_name="Rashid", email_address="gianna@gmail.com", phone_number=256789043)

#Seed participants
add_participant(first_name = "Loren", last_name = "Spears", email_address = "lorenspears@gmail.com", phone_number = 145800081, venue_id=1)
add_participant(first_name = "Jamal", last_name = "Oesteen", email_address = "jamaloesteen@gmail.com", phone_number = 986754734, venue_id=2)


#Seed venues



add_venue (name="Nairobi Cinema", location = "Nairobi", capacity = 500)
add_venue(name="Nairobi Hub", location="Westlands, Nairobi", capacity=90)
