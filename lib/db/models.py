from sqlalchemy import Integer, String, Text, create_engine, Column, ForeignKey, Boolean, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#Connect classes to the database using Base
Base = declarative_base()


session_participant = Table(
    "session_participant",
    Base.metadata,
    Column("session_id", Integer, ForeignKey("sessions.id")),
    Column("participant_id", Integer, ForeignKey("participants.id"))
)

class Organizer(Base):
    __tablename__ = "organizers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable = False)
    last_name = Column(String(40), nullable = False)
    email_address = Column(String)
    phone_number = Column(Integer, nullable = False)
    sessions = relationship("Session", back_populates="organizer")


class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    capacity = Column(Integer)
    participants = relationship("Participant", back_populates="venue")
    sessions = relationship("Session", back_populates="venue")