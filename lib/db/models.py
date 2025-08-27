from sqlalchemy import Integer, String, Text, create_engine, Column, ForeignKey, Boolean, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#Connect classes to the database using Base
Base = declarative_base()


mentorship_session_participant = Table(
    "mentorship_session_participant",
    Base.metadata,
    Column("mentorship_session_id", Integer, ForeignKey("mentorship_sessions.id")),
    Column("participant_id", Integer, ForeignKey("participants.id"))
)

class Organizer(Base):
    __tablename__ = "organizers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable = False)
    last_name = Column(String(40), nullable = False)
    email_address = Column(String)
    phone_number = Column(Integer, nullable = False)
    mentorship_sessions = relationship("MentorshipSession", back_populates="organizer")


class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    capacity = Column(Integer)
    participants = relationship("Participant", back_populates="venue")
    mentorship_sessions = relationship("MentorshipSession", back_populates="venue")


class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email_address = Column(String)
    phone_number = Column(Integer, nullable= False)
    venue_id = Column(Integer, ForeignKey("venues.id"))
    mentorship_sessions = relationship("MentorshipSession", secondary= mentorship_session_participant, back_populates="participants")
    venue = relationship("Venue", back_populates="participants")


class MentorshipSession(Base):
    __tablename__= "mentorship_sessions"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(String)
    description = Column(Text)
    organizer_id = Column(Integer, ForeignKey("organizers.id"), nullable=False)
    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=False)
    organizer = relationship("Organizer", back_populates="mentorship_sessions")
    venue = relationship("Venue", back_populates="mentorship_sessions")
    participants = relationship("Participant", secondary= mentorship_session_participant, back_populates="mentorship_sessions")

#Now connect the codes to the database
engine = create_engine("sqlite:///lib/db/mentorship.db")
#Now lets create the tables in the database
Base.metadata.create_all(bind=engine)
#Communicate with the database
Session = sessionmaker(bind=engine)
session = Session()

