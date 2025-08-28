# Mentorship Manager

A command-line application for managing mentorship programs efficiently. This tool allows you to create, view, update, and delete organizers, participants, venues, and mentorship sessions with a user-friendly CLI interface.

---

## Project Overview

This project allows full management of all entities—**Organizers**, **Participants**, **Venues**, and **Mentorship Sessions**—with the ability to create, view, update, and delete records in each table. Each entity is interconnected, allowing you to link organizers, participants, and venues to mentorship sessions for seamless scheduling.  

The application provides a user-friendly command-line interface (CLI) with clear prompts and color-coded feedback, making it easy to navigate through the various options. Input validation ensures that all records are accurate, while error messages guide you in correcting mistakes. This setup guarantees efficient coordination and management of all aspects of your mentorship program.

---

## Features

- **Organizer Management**
  - Add new organizers with their contact details.
  - View all organizers.
  - Update organizer information.
  - Delete organizers.

- **Participant Management**
  - Add participants with email addresses.
  - View all participants.
  - Update participant details.
  - Delete participants.

- **Venue Management**
  - Add new venues for sessions.
  - View, update, and delete venue details.

- **Mentorship Session Management**
  - Schedule new mentorship sessions by linking organizers, participants, and venues.
  - View all scheduled sessions.
  - Update session details.
  - Delete sessions.

- **Command Line Interface (CLI)**
  - Interactive prompts powered by **Click**.
  - Color-coded messages for success (green) and errors (red).

- **Database Integration**
  - Uses **SQLAlchemy ORM** for database operations.
  - Persistent storage in SQLite (`lib/db/mentorship.db`).

- **CRUD Operations**
  - Full **Create**, **Read**, **Update**, and **Delete** functionality across all entities.

- **Validation & Error Handling**
  - Ensures proper date, email, and phone number formats.
  - Clear, user-friendly error messages.

---

## Project Structure

```
phase-3-project-mentorship-manager/
│
├── lib/
  │ ├── db/
│ │ ├── crud.py # CRUD operations for all entities
│ │ ├── models.py # Database models using SQLAlchemy
│ │ ├── seed.py # Initial seed data for the database
│ │ └── mentorship.db # SQLite database file
│
│ ├── cli.py # Command-line interface with prompts and menus
│ ├── helpers.py # Helper functions used across the project
│ ├── main.py # Entry point for running the application
│
├── Pipfile # Python project dependencies
├── Pipfile.lock # Lock file for dependencies
└── README.md # Project documentation
```


## Installation

Follow these steps to set up and run the project locally:

### Clone the repository

gitgit clone <https://github.com/cherylmbani/phase-3-project-mentorship-manager>
cd phase-3-project-mentorship-manager

### Install dependencies using Pipenv
```bash
pip install pipenv # Install Pipenv if you don't have it already
pipenv install # Install project dependencies from Pipfile
```
### Activate the virtual environment
```bash
pipenv shell
```
### Set up the database

Ensure mentorship.db exists in lib/db/
If you need to seed the database with initial data, run:
```bash
python -m lib.db.seed
```
### Run the application
```bash
python main.py
```
## Usage

Run the application:


### How to Navigate

1. When the CLI starts, you will see a menu with options for:
   - Organizers
   - Participants
   - Venues
   - Mentorship Sessions
   - Exit
2. Choose an option by entering the corresponding number.
3. Follow the prompts to:
   - **Add** a new record by entering the required details.
   - **View** all records in a table.
   - **Update** an existing record by providing its ID and new details.
   - **Delete** a record by specifying its ID.

### Example Workflow
Choose organizer among the four groups of Mentorship Manager, select an option
Add a new organizer
Select "Organizer" → "Add Organizer"
Enter first name, last name, email, and phone number
Success message: "Organizer added successfully!"

Schedule a mentorship session
Select "Mentorship Session" → "Add Mentorship Session"
Provide title, date, description, venue ID, and organizer Id
Success message: "Mentorship session added successfully!"

View all participants
Select "Participants" → "View Participants"
The CLI will display a list of all participants with IDs and details

## Requirements

Before running this project, ensure you have the following installed on your system:

- **Python 3.8+**  
- **Pipenv** for dependency management. You can install it on your system by running the following commands:

```bash
pip install pipenv
pipenv install
```

## Contributing

We welcome contributions from the community! To contribute to this project, follow these steps:

1. **Fork the repository** and clone it to your local machine:

```bash
git clone <your-forked-repo-url>
cd phase-3-project-mentorship-manager
```
2. **Create a new branch for your feature or bug fix:**
```bash
git checkout -b feature-or-bugfix-name
```
3. **Make your changes and commit them with clear messages:**
```bash
git add .
git commit -m "Add feature or fix description"
```
4. **Push your branch to your forked repository:**
```bash
git push origin feature-or-bugfix-name
```
5. **Open a Pull Request on the main repository with a description of your changes.**
6. **Discuss, review, and make any requested changes. Once approved, your contribution will be merged.**

### Guidelines

Write clear, maintainable code.

Add comments where necessary.

Ensure that new code does not break existing functionality.

Follow existing code style and formatting conventions.

## License

This project is licensed under the **MIT License**.  

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
- The software is provided "as is", without warranty of any kind, express or implied.  

For more details, see the [LICENSE](LICENSE) file in the repository.


## Author

**Cheryl Mbani**  
GitHub: [https://github.com/cherylmbani](https://github.com/cherylmbani)  
Email: mbanicheryl45@gmail.com





