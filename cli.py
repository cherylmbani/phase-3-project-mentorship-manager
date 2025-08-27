#import click, the library for creating CLI applications
#Then import the crud functions to interact with
import click 
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
                if confirm:
                    delete_mentorship_session(session_id)
                    click.secho(f"Session {session_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")
        
        if choice == 2:
            click.secho("Choose the following organizer activities", fg="blue")
            click.secho("1. Add organizer", fg="green")
            click.secho("2. Update organizer details", fg="green")
            click.secho("3. View organizer details", fg="green")
            click.secho("4. Delete an organizer", fg="green")
            organizer_choice = click.prompt("Select an option", type=int)
            
            if organizer_choice==1:
                click.secho("fill in the following organizer details", fg="red")
                organizer_id = click.prompt("Please enter the Id of the organizer to update")
                first_name=click.prompt("First name")
                last_name=click.prompt("Last name")
                email_address=click.prompt("Email address")
                phone_number=click.prompt("Phone number")
                add_organizer(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number)
                click.echo(f"{first_name} {last_name}added successfully")

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
        

        if choice == 3:
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
                if confirm:
                    delete_mentorship_session(session_id)
                    click.secho(f"Session {session_id} deleted successfully", fg="blue")
                else:
                    click.secho("Deletion is cancelled", fg="purple")
        



        if choice ==5:
            click.secho("Exiting... Goodbye!", fg="magenta")
            break

if __name__=="__main__":
    main_menu()



