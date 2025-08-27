#import click, the library for creating CLI applications
#Then import the crud functions to interact with
import click 
from helpers import confirm_action, print_info
from lib.db.crud import(
    add_organizer,get_organizers, update_organizer, delete_organizer,
    add_participant, get_participants, update_participant, delete_participant,
    add_venue, get_venues, update_venue, delete_venue,
    add_mentorship_session, get_mentorship_sessions, update_mentorship_session, delete_mentorship_session

)
@click.group()
def cli():
    """Mentorship Manager"""
    pass

def main_menu():
    while True:
        click.secho("Mentorship Mnagaer", fg="blue", bold=True, underline=True)
        click.secho("1. Mentorship Session", fg="white")
        click.secho("2. Organizers", fg="white")
        click.secho("3. Participants", fg="white")
        click.secho("4. Venues", fg="white")
        click.secho("5. Exit", fg="white")
        choice = click.prompt("Select an option", type=int)
        
        #Full CRUD on Mentorship Sessions via CLI
        if choice == 1:
            click.secho("Choose the following mentorship session activities", fg="blue")
            click.secho("1. Add mentorship session", fg="green")
            click.secho("2. Update mentorship session", fg="green")
            click.secho("3. View mentorship session", fg="green")
            click.secho("4. Delete mentorship session", fg="green")
            mentorship_choice = click.prompt("Select an option", type=int)
            
            if mentorship_choice==1:
                click.secho("fill in the following fields of mentorship session to add", fg="red")
                mentorship_session_id = click.prompt("Please enter the Id of the session to Update")
                title=click.prompt("Session title")
                date=click.prompt("Session date(YYYY-MM-DD)")
                description=click.prompt("Session description")
                organizer_id=click.prompt("Organizer Id")
                venue_id=click.prompt("Venue Id")
                add_mentorship_session(title=title, date=date, description=description, organizer_id=organizer_id, venue_id=venue_id)
                click.echo(f"{title} added successfully")

            if mentorship_choice==2:
                mentorship_session_id= click.prompt("Please enter the id of the mentorship session to update")
                click.secho("Update the following fields of mentorship", fg="red")
                title=click.prompt("New session title", default="", show_default=False)
                date=click.prompt("New session date, YYYY-MM-DD",default="", show_default=False)
                description=click.prompt("New session description", default="", show_default=False)
                organizer_id=click.prompt("New organizer Id", default="", show_default=False)
                venue_id=click.prompt("New venue Id", default="", show_default=False)
                #a dictionary to collect the new/updated data
                updated_session={}
                if title:
                    updated_session["title"] = title
                if date:
                    updated_session["date"] = date
                if description:
                    updated_session["description"] = description
                if organizer_id:
                    updated_session["organizer_id"] = organizer_id
                if venue_id:
                    updated_session["venue_id"] = venue_id

                
                update_mentorship_session(mentorship_session_id, updated_session)
                click.secho(f"Session {mentorship_session_id} is updated successfully")

            if mentorship_choice==3:
                click.echo("These are the sessions registered")
                sessions = get_mentorship_sessions()
                if not sessions:
                    click.echo("Cannot retrieve sessions")
                else:
                    for s in sessions:
                        click.echo(f"ID: {s.id}")
                        click.echo(f"Title: {s.title}")
                        click.echo(f"Date: {s.date}")
                        click.echo(f"Description: {s.description}")
                        click.echo(f"Organizer Id: {s.organizer_id}")
                        click.echo(f"Venue Id: {s.venue_id}")
            
            if mentorship_choice==4:
                click.secho("Deleting a session", fg="red")
                session_id = click.prompt("Please enter the Id of the session to delete")
                confirm = click.prompt("Are you sure you want to delete this session(y/n)?", default=False)
                if confirm_action("Are you sure you want to delete this session?"):
                    delete_mentorship_session(session_id)
                    print_info(f"Session {session_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")
        
        #Full CRUD on Organizers via CLI
        if choice == 2:
            click.secho("Choose the following organizer activities", fg="blue")
            click.secho("1. Add organizer", fg="green")
            click.secho("2. Update organizer details", fg="green")
            click.secho("3. View organizer details", fg="green")
            click.secho("4. Delete an organizer", fg="green")
            organizer_choice = click.prompt("Select an option", type=int)
            
            if organizer_choice==1:
                click.secho("fill in the following organizer details", fg="red")
                organizer_id = click.prompt("Please enter the Id of the organizer to add")
                first_name=click.prompt("First name")
                last_name=click.prompt("Last name")
                email_address=click.prompt("Email address")
                phone_number=click.prompt("Phone number")
                add_organizer(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number)
                click.echo(f"{first_name} {last_name} added successfully")

            if organizer_choice==2:
                organizer_id=click.prompt("Please enter the Id of the organizer to update")
                click.secho("Update the following organizer fields", fg="red")
                first_name=click.prompt("New first name", default="", show_default=False)
                last_name=click.prompt("New last name",default="", show_default=False)
                email_address=click.prompt("New email address", default="", show_default=False)
                phone_number=click.prompt("New phone number", default="", show_default=False)
            
                #a dictionary to collect the new/updated data
                updated_organizer={}
                if first_name:
                    updated_organizer["first_name"] = first_name
                if last_name:
                    updated_organizer["last_name"] = last_name
                if email_address:
                    updated_organizer["email_address"] = email_address
                if phone_number:
                    updated_organizer["phone_number"] = phone_number
        
                update_organizer(organizer_id, updated_organizer)
                click.secho(f"Organizer {organizer_id} is updated successfully")

            if organizer_choice==3:
                click.echo("These are the organizers registered")
                organizers = get_organizers()
                if not organizers:
                    click.echo("Cannot retrieve organizers")
                else:
                    for o in organizers:
                        click.echo(f"ID: {o.id}")
                        click.echo(f"First name: {o.first_name}")
                        click.echo(f"Last name: {o.last_name}")
                        click.echo(f"Email address: {o.email_address}")
                        click.echo(f"Phone number: {o.phone_number}")
                        
            if organizer_choice==4:
                click.secho("Deleting an organizer", fg="red")
                organizer_id = click.prompt("Please enter the Id of the organizer to delete")
                confirm = click.prompt("Are you sure you want to delete this organizer(y/n)?", default=False)
                if confirm:
                    delete_organizer(organizer_id)
                    click.secho(f"Organizer {organizer_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")
        
        #Full CRUD on Participants Via CLI
        if choice == 3:
            click.secho("Choose the following participants activities", fg="blue")
            click.secho("1. Add participant", fg="green")
            click.secho("2. Update participant", fg="green")
            click.secho("3. View participants", fg="green")
            click.secho("4. Delete participant", fg="green")
            participant_choice = click.prompt("Select an option", type=int)
            
            if participant_choice==1:
                click.secho("fill in the following participant details", fg="green")
                participant_id = click.prompt("Please enter the Id of the participant to add")
                first_name=click.prompt("First Name")
                last_name=click.prompt("Last name")
                email_address=click.prompt("Email address")
                phone_number=click.prompt("Phone number")
                venue_id=click.prompt("Venue Id")
                add_participant(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number, venue_id=venue_id)
                click.echo(f"{first_name} {last_name} added successfully")

            if participant_choice==2:
                participant_id= click.prompt("Please enter the id of the participant to update")
                click.secho("Update the following fields of a participant", fg="red")
                first_name=click.prompt("New first name", default="", show_default=False)
                last_name=click.prompt("New last name",default="", show_default=False)
                email_address=click.prompt("New email address", default="", show_default=False)
                phone_number=click.prompt("New phone number", default="", show_default=False)
                venue_id=click.prompt("New venue Id", default="", show_default=False)
                #a dictionary to collect the new/updated data
                updated_participant={}
                if first_name:
                    updated_participant["first_name"] = first_name
                if last_name:
                    updated_participant["last_name"] = last_name
                if email_address:
                    updated_participant["email_address"] = email_address
                if phone_number:
                    updated_participant["phone_number"] = phone_number
                if venue_id:
                    updated_participant["venue_id"] = venue_id

                
                update_participant(participant_id, updated_participant)
                click.secho(f"Participant {participant_id} is updated successfully")

            if participant_choice==3:
                click.echo("These are the participants registered")
                participants = get_participants()
                if not participants:
                    click.echo("Cannot retrieve participants")
                else:
                    for p in participants:
                        click.echo(f"ID: {p.id}")
                        click.echo(f"First name: {p.first_name}")
                        click.echo(f"Last name: {p.last_name}")
                        click.echo(f"Email address: {p.email_address}")
                        click.echo(f"Phone number: {p.phone_number}")
                        click.echo(f"Venue Id: {p.venue_id}")
            
            if participant_choice==4:
                click.secho("Deleting a participant", fg="red")
                participant_id = click.prompt("Please enter the Id of the participant to delete")
                confirm = click.prompt("Are you sure you want to delete this participant(y/n)?", default=False)
                if confirm:
                    delete_participant(participant_id)
                    click.secho(f"Participant {participant_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")
        


        #Full CRUD Operations on Venues
        if choice == 4:
            click.secho("Choose the following venue activities", fg="blue")
            click.secho("1. Add venue", fg="green")
            click.secho("2. Update venue", fg="green")
            click.secho("3. View venues", fg="green")
            click.secho("4. Delete venue", fg="green")
            venue_choice = click.prompt("Select an option", type=int)
            
            if venue_choice==1:
                click.secho("fill in the following venue details", fg="green")
                venue_id = click.prompt("Please enter the Id of the venue to add")
                name=click.prompt("Name")
                location=click.prompt("Location")
                capacity=click.prompt("Capacity")
        
                add_venue(name=name, location=location, capacity=capacity)
                click.echo(f"{name} added successfully")

            if venue_choice==2:
                venue_id= click.prompt("Please enter the id of the venue to update")
                click.secho("Update the following fields of a venue", fg="red")
                name=click.prompt("New name", default="", show_default=False)
                Location=click.prompt("New location",default="", show_default=False)
                capacity=click.prompt("New capacity", default="", show_default=False)
            
                #a dictionary to collect the new/updated data
                updated_venue={}
                if name:
                    updated_venue["name"] = name
                if location:
                    updated_venue["location"] = location
                if capacity:
                    updated_venue["capacity"] = capacity

                
                update_venue(venue_id, updated_venue)
                click.secho(f"Venue {venue_id} is updated successfully")

            if venue_choice==3:
                click.echo("These are the venues registered")
                venues = get_venues()
                if not venues:
                    click.echo("Cannot retrieve venues")
                else:
                    for v in venues:
                        click.echo(f"ID: {v.id}")
                        click.echo(f"Name: {v.name}")
                        click.echo(f"Location: {v.location}")
                        click.echo(f"Capacity: {v.capacity}")
                        
            if venue_choice==4:
                click.secho("Deleting a venue", fg="red")
                venue_id = click.prompt("Please enter the Id of the venue to delete")
                confirm = click.prompt("Are you sure you want to delete this venue(y/n)?", default=False)
                if confirm:
                    delete_venue(venue_id)
                    click.secho(f"Venue {venue_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")



        if choice ==5:
            click.secho("Exiting... Goodbye!", fg="magenta")
            break

