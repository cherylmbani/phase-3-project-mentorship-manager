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
                    click.secho("Cannot retrieve sessions")


        if choice ==5:
            click.secho("Exiting..., Goodbye!", fg="magenta")
            break

if __name__=="__main__":
    main_menu()



